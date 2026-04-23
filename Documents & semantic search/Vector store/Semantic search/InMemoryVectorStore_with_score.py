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
        "Information about AI",    # Intentionally unrelated
        "How to greet in multi language",
        "how to create sample API response",
        "most useful information available",      #random gibbrish query
    ]

    for search in searches:
        print(f" query : {search}\n")
        
        results = vectore_store.similarity_search_with_score(search, k=2)

        for doc, score in results:
            relevance = "🟢 High" if score > 0.8 else "🟡 Medium" if score > 0.6 else "🔴 Low"
            print(f"   Score: {score:.4f} {relevance}")
            print(f"   Content: {doc.page_content[:60]}...")
            print(f"   metadata: {doc.metadata}\n")

        print("-"*80+"\n")

    print('='*80)
    print("\n key insights")
    print("   - Scores help filter out irrelevant results")
    print("   - Higher scores indicate stronger semantic similarity")
    print("   - Set thresholds based on your use case (e.g., >0.7 for relevance)")


if __name__ == "__main__":
    main()

        

    
