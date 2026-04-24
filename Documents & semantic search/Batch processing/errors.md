# Errors

1. `AttributeError: 'list' object has no attribute 'replace'`
   
```
   Cell In[1], line 43, in main()
     41 individual_embeddings = []
     42 for text in texts:
---> 43     embedding = embeddings.embed_query(texts)
   ```

solutions : embedding = embeddings.embed_query(text) #not (texts) because i m iterating over it.
