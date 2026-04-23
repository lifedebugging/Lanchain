# Vector stores

**what are vector stores?**

In very simple terms It's a sort of a storing mechanism an database specifically for storing and search embeddings so you thought but.

**A vector store doesn't just store embeddings. It stores embedded documents alongside the embeddings.**

1. Store: Add documents with their embeddings
2. Search: Find similar documents using vector similarity

<img width="588" height="144" alt="image" src="https://github.com/user-attachments/assets/b993d55c-da02-45f0-8dc7-66cfd210d438" />

*reference* : [langchain docs](https://docs.langchain.com/oss/python/integrations/vectorstores)

# Interface
LangChain provides a unified interface for vector stores, allowing you to:

    add_documents - Add documents to the store.
    delete - Remove stored documents by ID.
    similarity_search - Query for semantically similar documents.

This abstraction lets you switch between different implementations without altering your application logic.

# Intialize

To get started with vector store, provide it with embedding model.
```
from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embedding=SomeEmbeddingModel())
```
