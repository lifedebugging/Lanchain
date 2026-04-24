# The ovbservation:

the retriever Is fetching the right chunks at k=20. The earlier attempts were failing because k was too low.

**what does this tell you about choosing k in a production RAG system?**

 - it's about chunk size relative to document size. Smaller chunks mean more of them, so you need higher k to cover relevant sections.

But **higher k has a cost**. What is it?

Noise, the llm has to sort the output which will cost token and extra resources. 
the core RAG tradeoff — precision vs recall. Low k = fast but might miss relevant chunks. High k = better coverage but more noise and more tokens.

# Key Insights

**how to check if the RAG is actually working vs the LLM using it's own knowledge**?

For me I printed the chunks, compared the output to my [sample](sample_text.txt) text.

**Different queries and output**:

When I used the query("Give me the output of pangram setences")

I was getting this [pangram output](previous_ouput.txt) I blamed the model, I thought the retirever isn't fetching enough amount of right chunks.
So, I **increased** the **chunk_size** and **overlap** as well.

However It still wasn't getting the output from the material.

I changed the query and asked("tell me about short peom") 

and I got the [output](output.txt) as final answer and that confirmed that RAG is working, The poem is fake, the LLM couldn't know it from training data and it retrieved and returned it correctly.

Hence, `input`, `instruction`, `context` matters a lot in RAG.
