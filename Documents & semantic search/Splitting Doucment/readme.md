# Splitting Documents (chunking)

To understand What it means **chunking**, we gotta answer **why was splitting of documents required anyway?**

1. LLM context limits : Models have token limit (~4,000- 128,000 tokens) depending on the context size of the model, they can only process a certain amount of text at once. Feed too much -> it gets cut off or degrades in quality.
2. Relevance : Each chunk is meant to be larg enough to contain a useful idea, but small enough to be specific. This defines the precision of retieval.
3. cost : Smaller inputs = lower API costs.

## Chunk size trade offs

    small chunks (200-500 chars)           Large Chunks(1000-2000 chars)
    
    More precise                           More context
    Better for specific questions          Better for complex topics
    May lose context                       Less precise matching
    More chunks to process                 Fewer chunks

    
