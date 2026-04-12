from langchain_community.document_loaders import TextLoader
from pathlib import Path

#create sample data
data_dir = Path("./data")
data_dir.mkdir(exist_ok=True)

sample_text = """
Artificial Intelligence is the field of computer science focused on building 
systems that can perform tasks that normally require human intelligence.

Machine Learning is a subset of AI where systems learn from data rather than 
being explicitly programmed. Instead of writing rules, we feed examples and 
let the model discover patterns.

Deep Learning takes this further by using neural networks with many layers. 
These networks can learn complex representations of data, making them powerful 
for tasks like image recognition and language understanding.

Large Language Models (LLMs) are deep learning models trained on massive 
amounts of text. They learn the statistical patterns of language so well that 
they can generate coherent, contextually relevant responses.

Retrieval Augmented Generation (RAG) is a technique that combines LLMs with 
a knowledge base. Instead of relying solely on what the model learned during 
training, RAG fetches relevant documents at query time and feeds them as 
context — making answers more accurate and up to date.

Vector embeddings are numerical representations of text that capture semantic 
meaning. Similar concepts produce similar vectors, which is what allows a RAG 
system to find relevant documents through meaning rather than keyword matching.
"""
(data_dir / "ai_basics.txt").write_text(sample_text.strip())
#The .strip() method in Python is used to remove leading and trailing whitespace characters from a string. 
#It can also be customized to remove specific characters by passing them as an argument.

#Load the document
loader = TextLoader("./data/ai_basics.txt")
docs = loader.load()

print(f"Loaded {len(docs)} documents")
print(f"Content : {docs[0].page_content}")
print(f"Metadata : {docs[0].metadata}")
