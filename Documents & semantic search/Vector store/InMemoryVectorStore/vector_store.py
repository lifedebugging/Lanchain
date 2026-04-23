import os

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="all-MiniLM-L6-v2"
)



with open(r"D:\Downloads\sample_text.txt", encoding='utf-8') as f:
    docs = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap = 30,
    length_function=len,
)

text = text_splitter.create_documents([docs])

def main():
    
    print("Vector store and semantic search\n")

    print(f"Creating vector store with {len(docs)} documents. \n")


    #create vectore store
    vectore_store = InMemoryVectorStore.from_documents(text, embeddings)

    print(" Vector store created successfully\n")
    print("-"*80 + "\n")

    #Perform semantic searches
    searches = [
    {"query" : "Information about AI", "k" : 2},
    {"query" : "How to greet in multi language", "k" : 2},
    {"query" : "how to create sample API response", "k" : 2},
    {"query" : "most useful information available", "k" : 2},      #random gibbrish query
    ]

    for search in searches:
        query = search["query"]
        k = search["k"]
        print(f" search: '{query}' (top {k} results)\n")

        results = vectore_store.similarity_search(query, k=k)

        for i, doc in enumerate(results):
            print(f" {i +1}. {doc.page_content}")
            print(f"  Category: {doc.metadata}\n")

        print("-"*80+"\n")

    print('='*80)
    print("\n key insights")
    print(" - Vectore sotres enable fast similarity search over documents")
    print(" - Semantic search finds relevant content even without exact keyword matches")
    print(" - Metdata helps categorize and filter results")

if __name__ == "__main__":
    main()

        

    
