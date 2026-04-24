import os

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="all-MiniLM-L6-v2"
)

llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )

with open(r"D:\Downloads\sample_text.txt", encoding='utf-8') as f:
    docs = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap = 100,
    length_function=len,
)

text = text_splitter.create_documents([docs])

def main():
    
    print("Vector store and semantic search\n")

    print(f"Creating vector store with {len(docs)} documents. \n")


    #create vectore store
    vector_store = InMemoryVectorStore.from_documents(text, embeddings)

    print(" Vector store created successfully\n")
    print("-"*80 + "\n")

    #retriever
    query = "tell me the short poem"
    
    retriever = vector_store.as_retriever(k=20)
    final_retriever = retriever.invoke(query)

    chunks = []
    for doc in final_retriever:
        chunks.append(doc.page_content)

    print(chunks)

    #Passing the result to llm
    llm_invoke = llm.invoke(f"Given this context: {'\n'.join(chunks)} Answer this question: {query}")
    
    print(f"Final result: /n{llm_invoke.content}")
        
    print("-"*80+"\n")


if __name__ == "__main__":
    main()

        

    
