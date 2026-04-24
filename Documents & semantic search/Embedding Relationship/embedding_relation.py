import math
import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model= "all-MiniLM-L6-v2"
)

def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a * a for a in vec_a))
    magnitude_b = math.sqrt(sum(b * b for b in vec_b))
    return dot_product / (magnitude_a * magnitude_b)


def subtract_vectors(vec_a: list[float], vec_b: list[float]) -> list[float]:
    """Subtract two vectors."""
    return [a - b for a, b in zip(vec_a, vec_b)]


def add_vectors(vec_a: list[float], vec_b: list[float]) -> list[float]:
    """Add two vectors."""
    return [a + b for a, b in zip(vec_a, vec_b)]
    
def main():
    print(" Embedding Relationships: Vector Math Demo\n")
    print("This demonstrates how embeddings capture semantic relationships")
    print("that can be manipulated mathematically.\n")
    print("=" * 70 + "\n")

    # ============================================================================
    # Example 1: Animal Life Stages
    # Demonstrating: Puppy - Dog + Cat ≈ Kitten
    # ============================================================================

    print("🐶 Example 1: Animal Life Stages")
    print("─" * 70)
    print("\nTesting: Embedding('Puppy') - Embedding('Dog') + Embedding('Cat')")
    print("Expected result: Should be similar to Embedding('Kitten')\n")

    # Generate embeddings for animals and their young
    animal_texts = ["Puppy", "Dog", "Cat", "Kitten"]
    animal_embeds = embeddings.embed_documents(animal_texts)
    puppy_embed, dog_embed, cat_embed, kitten_embed = animal_embeds

    # Perform vector arithmetic: Puppy - Dog + Cat
    puppy_minus_dog = subtract_vectors(puppy_embed, dog_embed)
    result_vector = add_vectors(puppy_minus_dog, cat_embed)

    # Compare result with actual kitten embedding
    similarity_to_kitten = cosine_similarity(result_vector, kitten_embed)

    # Also compare with other options
    similarity_to_cat = cosine_similarity(result_vector, cat_embed)
    similarity_to_dog = cosine_similarity(result_vector, dog_embed)
    similarity_to_puppy = cosine_similarity(result_vector, puppy_embed)

    print("Results (higher = more similar):")
    print(f"   Similarity to 'Kitten': {similarity_to_kitten:.4f} ← Expected winner!")
    print(f"   Similarity to 'Cat':    {similarity_to_cat:.4f}")
    print(f"   Similarity to 'Dog':    {similarity_to_dog:.4f}")
    print(f"   Similarity to 'Puppy':  {similarity_to_puppy:.4f}")

    if similarity_to_kitten > max(similarity_to_cat, similarity_to_dog, similarity_to_puppy):
        print("\n✅ Success! The vector math correctly identified 'Kitten'!")
    else:
        print("\n⚠️  The result is close, but not the highest match to 'Kitten'")

    print("\n" + "=" * 70 + "\n")

    # ============================================================================
    # Example 2: Semantic Relationships
    # ============================================================================

    print("📚 Example 2: Semantic Similarity Clusters")
    print("─" * 70 + "\n")

    # Create semantic clusters
    tech_texts = ["Python programming", "JavaScript coding", "Software development"]
    animal_texts = ["Golden retriever dog", "Siamese cat", "Pet hamster"]
    food_texts = ["Italian pizza", "Japanese sushi", "Mexican tacos"]

    all_texts = tech_texts + animal_texts + food_texts
    all_embeds = embeddings.embed_documents(all_texts)

    print("Comparing items across categories:\n")

    # Compare first item of each category
    tech_animal = cosine_similarity(all_embeds[0], all_embeds[3])
    tech_food = cosine_similarity(all_embeds[0], all_embeds[6])
    animal_food = cosine_similarity(all_embeds[3], all_embeds[6])
    tech_tech = cosine_similarity(all_embeds[0], all_embeds[1])
    animal_animal = cosine_similarity(all_embeds[3], all_embeds[4])
    food_food = cosine_similarity(all_embeds[6], all_embeds[7])

    print("Within-category similarities (should be high):")
    print(f"   'Python' vs 'JavaScript':      {tech_tech:.4f}")
    print(f"   'Dog' vs 'Cat':                {animal_animal:.4f}")
    print(f"   'Pizza' vs 'Sushi':            {food_food:.4f}")

    print("\nCross-category similarities (should be lower):")
    print(f"   'Python' vs 'Dog':             {tech_animal:.4f}")
    print(f"   'Python' vs 'Pizza':           {tech_food:.4f}")
    print(f"   'Dog' vs 'Pizza':              {animal_food:.4f}")

    print("\n" + "=" * 70)
    print("\n💡 Key Insights:")
    print("   - Embeddings encode semantic relationships as vector dimensions")
    print("   - Similar concepts cluster together in vector space")
    print("   - Vector math can reveal analogies (Puppy:Dog :: Kitten:Cat)")
    print("   - This enables powerful semantic reasoning in AI applications")


if __name__ == "__main__":
    main()
