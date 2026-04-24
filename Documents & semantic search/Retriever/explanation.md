# Expalantion of as_retriever 
```
retriever = vector_store.as_retriever(k=5)
    final_retriever = retriever.invoke(query)
```
This is our R in **RAG**, the final retriever. `vectorstore.as_retrievers` is traditionaly retreiver inbuilt in vector stores.

Where, `k` is determines the **Top K** result.

and finally invoking the retriever ` retriever.invoke` with `(query)` and storing the result in `final_retriever`.

but **what does `retriever.invoke()` return**?

answer is a list of `Document` objects.

so to get all the answer(page_content) from that list. you need to iterate over the `final_retriever`.

we ran into an error here check out [error](error_log.txt)


```
chunks = []
    for doc in final_retriever:
        chunks.append(doc.page_content)
```

here, looping over `final_retriever` and adding the `page_content` via `append` and storing in `chunks`

where, `chunks` at first contain nothing it's an **empty list** `chunks = []`

Now we have the result.

Next is **connect the retriever output to an LLM and get a real generated answer, not just retrieved chunks**.

  # Note
  
  You don't invoke the llm once per chunk. We need one final answer from all retrieved chunks combined.

```
llm_invoke = llm.invoke(f"Given this context: {'\n'.join(chunks)} Answer this question: {query}")
    
    print(llm_invoke.content)
```
here we invoke the llm and pass it the context and the query via the `prompt`.

but the context provided to llm is a list, it's a not string, and `llm` works best with `string` so to convert it into string.

we doing `{'\n'.join(chunks)}` at first I thought of doing:

   final_chunk = str(chunk)

but the **problem** is : **It converts the whole list to a string with brackets and quotes. That's messy.**

where, On` "\n".join(chunks)` — join() takes a list and combines it into one string, with "\n" as the separator between each item. str(chunks) gives you ['chunk1', 'chunk2'] with brackets and quotes. Messy vs clean.


end.
