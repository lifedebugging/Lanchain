# Batch procesing

Batch processing is a embedding method where we create embeddings in a big chunk as a `batch` using `embed_documents` it is considered 
faster than any other embedding method for large datasets.

**Key Takeaways**:

1. Batch procesing may perform typically faster
2. It reduces API calls hence, lower costs.
3. Batch processing is easy to implement via `embed_documents()`
4. The internal processing may vary from other embedding processing creating slightly difference in embedding values.
