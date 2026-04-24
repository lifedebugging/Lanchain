# Embedding Relationship

**what is Embedding relationship**?

The relationship between the embedded values in a given vector store it's about how close (similar) and  far(distinct) the meanings are.

The code shows why ` Puppy - Dog + Cat = Kitten` works mathematically.

To undersatand how we have to answer **what is the subtraction actually doing to the vector**?

**Answer**: Dog and Puppy are related by one thing - age/maturity. When you subtract `Dog` from `Puppy`, you're isolating that realationship. You're
left with a vector that roughly means "youngoness" or "the young version of"

Then you add that to `Cat`. You get the yougness of the Cat.

# Insights
That shows the embedding space captures realtionships as directions. Substraction isolates a relationship, addition applies it somwhere else.

# Key observation

The [code](embed_relation.py) uses `zip` version for calculating cosine product. 

However, I prefer `np.dot` with numpy.

**Reason**:
1. Numpy is several times faster for vector and matrices calculation at given at day.
2. Numpy handles the cosine and all the math behind it automatically.
3. It is easier to implement.

   ```
   def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
   ```
   
Where, `zip` is manual, pure Python, slower.


# Note
This exercise exists to show you *why* vector stores work- the math underneath.

This code is a *reference* from [Microsoft-langchain-repository](https://github.com/microsoft/langchain-for-beginners/blob/main/07-documents-embeddings-semantic-search/code/09_embedding_relationships.py)
   
