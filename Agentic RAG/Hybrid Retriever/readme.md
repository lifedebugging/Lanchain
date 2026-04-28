# observation

**Ensemble Retreiver is a part of langchain_classic.**

```
from langchain_classic.retrievers import EnsembleRetriever
```

# Explanation
The script is a complete working async agentic RAG.
It decides when to use it's tool to search from the material. For general questions it is given instruction to answer without using the tool.

Which makes it's **agentic rag**.

**Note** : `system_prompt` is a big deal during agentic rag implementation or any external tool implementaion. Make sure to:
1. Describe the tools discription properly
2. system_prompt with role, constraints and output.
3. if your question is general and you still want answer from material, specify that when `querying` the agent.

# Important coding blocks
1. Document loader used :

   `PyPDFLoader(..)`
2. Splitting documents via :

  ```
   splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
     model = "model_name",
     chunk_size = int
     chunk_overlap = int
   )

 splitted_documents = splitter.split_documents(documents)
   ```

 **Note**: This split document using `token` instead of `characters`
 
3. Embeddings used: `HuggingFaceEmbedding` from `langchain_huggingface`

   ```
   embeddings = HuggingFaceEmbeddings(
    model = "all-MiniLM-L6-v2"
   )
   ```
4. vector store used: Chroma

   ```
   vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="D:/Downloads/",
   )

   vector_store.add_documents(documents=splitted_documents)
   ```
   **persist_directory** params decide where the db is been created and saved permanently.
   
   **note** : you can also use Chroma cloud and define `id` for more control over **database**.

5. Two retriever used: **BM25** and **Chroma Builtin**:

   ```
   m25_retriever = BM25Retriever.from_documents(
    splitted_documents,
    k=5,
    preprocess_func=word_tokenize,
   )

   #chroma builtin retriever
   chroma_retriever = vector_store.as_retriever(
   search_type="similarity",
   search_kwargs={"k":5},
   )
   ```
   **bm25** is a keyword based retriever where as **chroma retriever** uses **similarity** based search.

   You can explicitly define the `search_type` inside `as_retiever()` for **chroma**.

6. merging retriever search result via `EnsembleRetriever`

   ```
   ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, chroma_retriever],
    weights = [0.5, 0.5],
    c= 60,
   )
   ```

7. Created tool that takes `str` as query and returns `str`

   ```
   @tool
   async def search_docs(query: str) -> str:
    """
    "Search documentation provided for specific information about AI. 
    Use this when you need factual information from the material you've been provided.
    """
    result = await ensemble_retriever.ainvoke(query)
    
    chunks = []
    for doc in result:
        chunks.append(doc.page_content)
        
    return "\n\n".join(chunks)
    ```
   **Note**: since the object produced by retriever is a `list of documents` we're using `"\n\n".join()` to convert the `list` to `str`.

Rest is just agent and invokation of the agent.

    

   
   
# reference

1. [EnsembleRetriever](https://reference.langchain.com/python/langchain-classic/retrievers/ensemble/EnsembleRetriever)
2. [arank_fusion](https://reference.langchain.com/python/langchain-classic/retrievers/ensemble/EnsembleRetriever/arank_fusion)
3. [chroma db](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma)

