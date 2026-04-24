# The ovbservation:

the retriever Is fetching the right chunks at k=20. The earlier attempts were failing because k was too low.

**what does this tell you about choosing k in a production RAG system?**

 - it's about chunk size relative to document size. Smaller chunks mean more of them, so you need higher k to cover relevant sections.

But **higher k has a cost**. What is it?

Noise, the llm has to sort the output which will cost token and extra resources. 
the core RAG tradeoff — precision vs recall. Low k = fast but might miss relevant chunks. High k = better coverage but more noise and more tokens.

