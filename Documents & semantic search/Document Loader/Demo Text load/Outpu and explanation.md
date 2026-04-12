# Output 

    Loaded 1 documents
    Content : Artificial Intelligence is the field of computer science focused on building 
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
    Metadata : {'source': './data/ai_basics.txt'}

# How it works:

1. To create sample data : We write a text file to `./data/ai_basics.txt`
2. Initialize TextLoader : Pass the file path to the loader.
3. Load : Call `loader.load()` to read the file.
4. result : Returns a list of Document objects.

# Points to note:

1. TextLoader reads text files and handles file I/O.
2. Return list of Document objects (even for single files, for consistency)
3. Meta data automatically includes the source file path.

# What comes out?

A Document object with two things:

          Field                    What it holds page_content The actual text 
          metadata                  Where it came from (source, page, etc.)

# The flow so far :

       your_file.txt
             ↓
        TextLoader  
             ↓
    Document(page_content, metadata)  <-here
             ↓
    chunking → embedding → storage
    
# mistakes to avoid :

1. from langchain_community.document_loader❌ - it should be .document_loaders ✅
2. langchain_community module not found - python -m pip install langchain_community
