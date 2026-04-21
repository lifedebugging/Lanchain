import math
import os

import numpy as np

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

    
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


    
def main():
    print("Basic embeddings examples\n")

    texts = [
        "LangChain makes building AI apps easier",
        "LangChain simplifies AI application development",
        "I love eating pizza for dinner",
        "The weather is sunny today",
    ]

    print("Creating embeddings for texts...\n")

    all_embeddings = embeddings.embed_documents(texts) 

    print(f" Created {len(all_embeddings)} embeddings")
    print(f"   Each embedding has {len(all_embeddings[0])} dimensions\n")

    print("First embedding (first 10 values):")
    print(all_embeddings[0][:10])
    print("End of first embedding\n")


    # Compare similarities
    print("Similarity Comparisons:\n")

    pairs = [
        (0, 1, "LangChain vs LangChain (similar meaning)"),
        (0, 2, "LangChain vs Pizza (different topics)"),
        (0, 3, "LangChain vs Weather (different topics)"),
        (2, 3, "Pizza vs Weather (both different from LangChain)"),
    ]
    
    for i, j, description in pairs:
        similarity = cosine_similarity(all_embeddings[i], all_embeddings[j])
        print(f"{description}:")
        print(f"   Score: {similarity:.4f}")
        print(f'   Texts: "{texts[i]}" vs "{texts[j]}"\n')

    print("=" * 80)
    print("\n Key Insights:")
    print("   - Similar meanings → High similarity scores (>0.8)")
    print("   - Different topics → Low similarity scores (<0.5)")
    print("   - Embeddings capture semantic meaning, not just keywords!")


if __name__ == "__main__":
    main()

    
    

    

    

    
    

               
