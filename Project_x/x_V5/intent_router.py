import re
import json
import math
import nltk
import unicodedata
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from scipy.special import expit as sigmoid
from intent_registery import INTENT_REGISTRY
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from scipy.special import expit as sigmoid
from langchain_classic.retrievers import EnsembleRetriever
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import CrossEncoder

"""
This is a json file used as a dataset
in semantic router
"""
with open('D:/Documents/Project_x/x v5/janus_semantic_registry_v8.json', 'r', encoding='utf-8') as file:
    semantic_dataset  = json.load(file)
    
    
#stopwords
"""
Here is used nltk corpus for stopwords removal
There contain some pre defined stopwords
"""
stop_words = set(stopwords.words('english'))

#embedding model
"""
HuggingFace embedding model is used for embedding vectors
"""
embeddings = HuggingFaceEmbeddings(
    model="all-MiniLM-L6-V2"
    )
    
#encoder model
"""
A Cross encoder model used after retrieval as a scoring system
"""

encoder_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

#document preparation for semantic router
"""
This is a document preparation process 
iterating over semantic dataset to create 'Document'
and storing in below variables
"""

page_data = []
meta_data = []
documents = []

for item in semantic_dataset:
    meta_data = item["name"]
    page_data = " ".join(item["positive_examples"])
    new_data = Document(
        page_content= page_data,
        metadata = {"category": meta_data}
        )
    documents.append(new_data)
    
#vector store embeds building
"""
InMemoryVectorStore is a standard storage method 
uses ram for storage.
Builds the embedding stroage.
"""

vector_store = InMemoryVectorStore.from_documents(
documents, 
embeddings,
)

#retriever
"""
embeddings retriever using
as_retriever standard module for retrieving embeddings.
"""

embed_retriever = vector_store.as_retriever(k=5)


#filtering function for bm25 preprocess function
"""
Preporcess function created solely for used by bm25 retrievers
It filters the query string in various ways
such as lower casing, filtering out the stopwords
"""

def Preproccessing(query: str):
    # normalization
    normalized_uni_query = unicodedata.normalize('NFKC', query)
    # lower case
    tokens = word_tokenize(normalized_uni_query.lower())
    # filter
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

    return filtered_tokens 

#bm25 document building
"""
bm25 retriever defined with k = 5 value.
and custom preprocess function
"""

bm25_retriever  = BM25Retriever.from_documents(
    documents,
    k = 5,
    preprocess_func=Preproccessing
    )

ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, embed_retriever],
    weights=[0.5, 0.5],
    c=60,
)
    
# keyword router refined
"""
A keyword mapping function
goes through all the keywords in keyword_registry
append the category
"""

# def build_keyword_map():
#     keyword_map = {}
#     for category, data in INTENT_REGISTRY.items():
#         for keyword in data["keywords"]:
#             if  keyword in keyword_map:
#                 keyword_map[keyword].append(category)
#             else:
#                 keyword_map[keyword] = [category]
    
#     return keyword_map

# keyword_map = build_keyword_map()
"""
This calculates how many categories a keyword appears in.
"""    
# # IDf weight
# def compute_idf(keyword_map, N):
#     idf = {}
#     for keyword in keyword_map.items():
#         df = len(keyword_map[keyword])
#         idf[keyword] = math.log(N /df)
#     return idf
    
# N = len(INTENT_REGISTRY)
# idf = compute_idf(keyword_map, N)
    
# Filtering
"""
This is a filtering function similar to preprocessing function
However this one is requires to flat down query to keywords only
using the three different types of filteration method
the result of the is function will be used in keyword_intent
to calculate confidence"""

def filtering(query: str):

    # normalization
    normalized_uni_query = unicodedata.normalize('NFKC', query)
    # lower case
    tokens = word_tokenize(normalized_uni_query.lower())
    # filter
    filtered_tokens = [
        word for word in tokens 
        if word.isalpha() and word not in stop_words]

    return filtered_tokens #list required for counting meaningful words in denominator.

 
 #normalization    
def normalization(query : str):
    stripped_query = query.lower().strip()
    dup_query = re.sub(r'([!?.,;:])\1+', r'\1', stripped_query)
    normalized_uni_query = unicodedata.normalize('NFKC', dup_query)
    
    return normalized_uni_query 


#keyword searching for intent
def keyword_intent(query : str, top_k: int=1)-> list[dict]:
    """
    Classify a user query against the intent registry.
    
    Args:
    query: The user query string
    top_k: Number of top categories to return (default 1 for hard routing)
    
    Returns:
    List of dicts with category, confidence, model, priority, tools.
    Empty list if no match(fall through to semantic search).
    """ 
    user_query = normalization(query)
    filtered_token = filtering(query)
    
    #step 1 - The multi-keyword scan
    for category, data in INTENT_REGISTRY.items():
        matched = []
        score = []
        for keyword in data["keywords"]:
            if re.search(r'\b'  + re.escape(keyword) + r'\b', user_query):
                weight = len(keyword.split())
                score.append(weight)
                matched.append(keyword)
                    
        # priority = int(data.get("priority", 5))
    
        if len(filtered_token) == 0:
            return []
        
        #step 2 - scores for each directory
        scores = {}
        
        # Find the confidence
        confidence = sum(score) / len(filtered_token)        
        if confidence >= 0.70:
            scores[category] = {
                "category": category,
                "confidence": round(min(confidence, 0.99), 2),
                "model": data["model"],
                "tool": data["tool"],
                "priority": data["priority"],
                "matched_keywords": matched[:2]
            }

        #sort by confidence descending
        sorted_scores = sorted(scores.values(), key=lambda x: x["confidence"], reverse=True)
        return sorted_scores[:top_k]

    
def semantic_intent(query: str):
    results = ensemble_retriever.invoke(query)
    
    if len(results) == 0:
        return []
    else:
        normalize_description = {item["name"]: item["description"] for item in semantic_dataset}

        scores = []

        for item in results:
            last_item = item.metadata['category']
            lookup = normalize_description[last_item]                    
            cross_encoder = encoder_model.predict([[query, lookup]])
            scores.append((last_item, cross_encoder))
        
        scores.sort(key= lambda x: x[1][0], reverse=True) 

        raw_scores = np.array([s[1][0] for s in scores])
        names = np.array([s[0] for s in scores])
        confidence = sigmoid(raw_scores)
        round_confidence = np.round(confidence, 3)
        zipped = zip(names, round_confidence)
        zipper = list(zipped)


        winner = []

        normalized_threshold = {item["name"] : item["threshold"] for item in semantic_dataset}
            
        gap = zipper[0][1] - zipper[1][1]
        final_item = zipper[0][0]
        final_lookup = normalized_threshold[final_item]
        print(gap)
        print(final_lookup)
        if zipper[0][1] > final_lookup and gap >= 0.3:
            winner.append(zipper)

        return winner