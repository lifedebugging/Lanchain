import os
import time

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model= "all-MiniLM-L6-v2"
)

def main():
    print(" Batch Embeddings\n ")

    texts = [
        "Machine learning is a subset of artificial intelligence that enables systems to learn from experience without being explicitly programmed.", 
        "Supervised learning trains on labeled datasets where each input is paired with a corresponding output.", 
        "Unsupervised learning discovers hidden patterns in unlabeled data through techniques like clustering and dimensionality reduction.", 
        "Neural networks consist of layers of interconnected nodes inspired by the biological structure of the human brain.", 
        "Deep learning uses networks with many hidden layers to automatically extract complex hierarchical features from raw data.",
        "Gradient descent minimizes the loss function during training by iteratively adjusting model weights in the direction of steepest descent.", 
        "Overfitting occurs when a model captures noise alongside the underlying pattern, leading to poor generalization on unseen data.", 
        "Regularization techniques such as L1, L2 penalties, dropout, and early stopping are used to combat overfitting.", 
        "Transfer learning leverages knowledge from one task to improve performance on a related task, reducing data and compute requirements.", 
        "Embeddings are dense vector representations of data that capture semantic meaning, commonly used in NLP and recommendation systems.",
    ]

    #Method 1 : Batch embedding
    print(" method 1 : good ol'batch embedding with embed_documents()")
    start_time = time.time()
    batch_embeddings = embeddings.embed_documents(texts)
    batch_time = time.time() - start_time

    print(f" Created {len(batch_embeddings)} embeddings in {batch_time:.2f}s")
    print(f" Dimension per embedding: {len(batch_embeddings[0])}\n")

    #Method 2 : Individual embedding
    print("Method 2 : Individual embedding 'string-by-string' with embed_query()")
    start_time = time.time()
    individual_embeddings = []
    for text in texts:
        embedding = embeddings.embed_query(text)
        individual_embeddings.append(embedding)
    individual_time = time.time() - start_time

    print(f" Created {len(individual_embeddings)} embeddings in {individual_time:.2f}s\n")

    #compare performance
    print("-"*80 + "\n")
    print(" performance comparison")
    print(f"   Batch method:      {batch_time:.2f}s")
    print(f"   Individual method: {individual_time:.2f}s")

    if individual_time > batch_time:
        speedup = individual_time / batch_time
        print(f"\n Batch processing is {speedup:.1f}x faster")
    else:
        print(f"\n NOte: For small batches, performance may be similar")


    print("\n" + "=" * 80)
    print("\n💡 Key Insights:")
    print("   - Use embed_documents() for multiple texts (batching)")
    print("   - Use embed_query() for single queries")
    print("   - Batching reduces API calls and improves efficiency")
    print("   - Consider rate limits when processing large datasets")

if __name__ == "__main__":
    main()
