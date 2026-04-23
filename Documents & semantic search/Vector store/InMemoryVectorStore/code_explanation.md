# Dependencies 
`from langchain_core.documents import Document`

`from langchain_huggingface import HuggingFaceEmbeddings`

`from langchain_core.vectorstores import InMemoryVectorStore`

`from langchain_text_splitters import RecursiveCharacterTextSplitter`


# Embedding model

```
embeddings = HuggingFaceEmbeddings(
    model="all-MiniLM-L6-v2"
)
```
Better than configurating a OpenAIEmbeddingModel or anything else, I will cross the bridge when I get there.

# Loading document and splitting

```
with open(r"D:\Downloads\sample_text.txt", encoding='utf-8') as f:
    docs = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap = 30,
    length_function=len,
)

text = text_splitter.create_documents([docs])
```

**The documents used**:  [sample_text](sample_text.txt).

**Text splitter used** : `RecursiveCharacterTextSplitter` check out `splitter` folder to learn more about **text splitters**.

# INMemoryVectorStore

`vector_store = InMemoryVectorStore.from_documents(text, embeddings)`

This is where we are creating instance of our vector storage feeding it `text` which is the document content and `embeddings` is the variable containing instance of 
embedding model we're using `HuggingFaceEmbedding`.

```
searches = [
    {"query" : "Information about AI", "k" : 2},
    {"query" : "How to greet in multi language", "k" : 2},
    {"query" : "how to create sample API response", "k" : 2},
    {"query" : "most useful information available", "k" : 2},      #random gibbrish query
    ]
```

`searches` has list and inside is dictionary with two attributes `query` and `k`. Demonstrating that `k` is configurable.

Where `k` is **Top K** search: It retreives the top `k` results.

In real cases a summarizer might need k=10 or k=20 to pull enough chunks to cove rthe full document. Hence `k` depends on the use case. There's no universal right answer.

**Note**: `k` used in chatbot and agents are low maybe k=1 or 2.

# Similarity search
```
for search in searches:
        query = search["query"]
        k = search["k"]
        print(f" search: '{query}' (top {k} results)\n")

        results = vector_store.similarity_search(query, k=k)

        for i, doc in enumerate(results):
            print(f" {i +1}. {doc.page_content}")
            print(f"  Category: {doc.metadata}\n")
```
Here, 
```
for search in searches:
        query = search["query"]
        k = search["k"]
        print(f" search: '{query}' (top {k} results)\n")
```
This is just a for loop iterating over each query in searches, so `query = search["query"]`

Similarly iterating over each `k` assigned to each query, `k = search["k"]`

and printing the search.

 **similarity_search**: `results = vector_store.similarity_search(query, k=k)`

This is where similarity search is happening it's a part of vector_store class.

```
for i, doc in enumerate(results):
            print(f" {i +1}. {doc.page_content}")
            print(f"  Category: {doc.metadata}\n")
```
Here, iterating over the results using `enumerate` to print the indexing.
This prints the content inside the document and it's metadata.

**Note**: Check [output](output.txt) to see the result.

end.
