# Embeddings

# what are Embeddings?

Embeddings convert text into numerical vectors that capture semantic meaning, that's it:
1. Similar concepts -> Similar vectors
2. "cat" - "dog" -> "animal", "domestic", "pets" etc.
   
![image.png](attachment:30003c07-0f11-4119-ad8e-5491ad2d4d79.png)

*Embeddings map text to points in semantic space where similar meanings are close together.*

*reference* - Github/langchain-for-beginners


**Embedding models transform raw text—such as a sentence, paragraph, or tweet—into a fixed-length vector of numbers that captures its semantic meaning.
These vectors allow machines to compare and search text based on meaning rather than exact words.**

# How it works

    Vectorization — The model encodes each input string as a high-dimensional vector.
    Similarity scoring — Vectors are compared using mathematical metrics to measure how closely related the underlying texts are.

# Similarity metrics

**Several metrics are commonly used to compare embeddings**:

    Cosine similarity — measures the angle between two vectors.
    Euclidean distance — measures the straight-line distance between points.
    Dot product — measures how much one vector projects onto another.

