# what changed?
Unlike Version 1 this version hsa better error handling and hybrid retriever.

What's better is in previous version it created the file many times over each run of script.

# Fix

Now it has a better logic function to decide whether to use existing **Chroma** or create a new one at specified *`persist_directory`*.

