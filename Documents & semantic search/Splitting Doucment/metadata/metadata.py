from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import json

def main():
    docs = [
        Document(
            page_content = """
            LangChain is a framework for building AI applications. It provides abstractions
for working with language models, vector stores, and chains. The framework supports
multiple LLM providers including OpenAI, Anthropic, and Azure.
            """.strip(),
            metadata={
                "source": "langchain-intro.md",
                "category": "tutorial",
                "difficulty": "beginner",
                "date": "2024-01-15",
                "author": "Tech Team",
                "tags": ["langchain", "python", "ai"],
            },
        ),
        Document(
            page_content="""
RAG (Retrieval Augmented Generation) systems combine document retrieval with
language model generation. This approach allows LLMs to access external knowledge
and provide more accurate, contextual responses without retraining the model.
            """.strip(),
            metadata={
                "source": "rag-explained.md",
                "category": "concept",
                "difficulty": "intermediate",
                "date": "2024-02-20",
                "author": "AI Research Team",
                "tags": ["rag", "retrieval", "llm"],
            },
        ),
        Document(
            page_content="""
Vector databases store embeddings and enable semantic search. Unlike traditional
keyword search, semantic search understands meaning and context. Popular vector
databases include Pinecone, Weaviate, and Chroma.
            """.strip(),
            metadata={
                "source": "vector-db-guide.md",
                "category": "infrastructure",
                "difficulty": "intermediate",
                "date": "2024-03-10",
                "author": "Data Team",
                "tags": ["vectors", "embeddings", "database"],
            },
        ),
    ]
    print(f"Number of docs {len(docs)}")

    #display documents and their metdata
    for i, doc in enumerate(docs):
        print(f"Document {i+1}")
        print("-" * 70)
        print("content:", doc.page_content[:80] + "...")
        print("\nMetadata:")
        print(json.dumps(doc.metadata, indent=2))
        print("\n")

        print("="*70)
        print("\n Splitting documents (meta data is preserver):\n")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
        )

        split_doc = splitter.split_documents(docs)
        print(f"split {len(docs)} documents into {len(split_doc)}")

        #showin each chunks with metdata
        for i,doc in enumerate(split_doc[:3]):
            print(f"chunk {i+1}")
            print(f"content : {doc.page_content}")
            print(f"Source : {doc.metadata.get("source")}")
            print(f"category : {doc.metadata.get("category")}")
            print(f"Tags : {doc.metadata.get("tags")}")
            print()

        #filter document by metadata
        print("-"*70)
        print("\n Filtering by metadata")

        beginner_docs = [
            doc for doc in docs if doc.metadata.get("difficulty") == "beginner"
        ]
        print(f"Beginner documents : {len(beginner_docs)}")
        for doc in beginner_docs:
            print(f" -{doc.metadata.get("source")}")

        ai_docs = [
            doc for doc in docs if "ai" in doc.metadata.get("tags", [])
        ]
        print(f"\n Documents tagged 'ai' : {len(ai_docs)}")
        for doc in ai_docs:
            print(f" -{doc.metadata.get("source")}")

        print("\n Metadata is essentail for oranizing and filtering documents")

if __name__ == "__main__":
    main()
            
        
            
