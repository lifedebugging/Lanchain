# Explanation of [metadata.py](metadata.py)

**Use cases of Document and json imports**

 **Document** (from LangChain): This is the "Standard Container" for text. Any time you pass text to LangChain (to be indexed, summarized, or chatted with), you usually wrap it in a Document object. It pairs the text with its source info.
 
 **json** (Standard Python): This is just a formatting tool. It's used here to make the metadata dictionary look nice (pretty-printed) when you print it to the console.

# part 1
```
Document(
            page_content = """
            LangChain is a..
            metdata = ...
            )
```

# Do we actually need to split data manually?
No. Usually, you don't. 

1. **Normal Way**: You use a Loader.
   ```
   loader = TextLoader("my_file.txt")
   docs = loader.load() # This creates the Document objects for you
   ```
2. **Manual way**: We are creating `Document` objects by hand because we're writing a demo with fake data. It works for learning but not recommended in real use case. Normally used `DirectoryLoader`, `WebBaseLoader`, etc.

**But why *Loader* recommended**?

Because when you use a loader, it automatically creates metadata (like source="my_file.txt"). When you split the document, LangChain *automatically* copies the metadata to the new chunks. You don't have to do it manually.

# part 2

```
 for i, doc in enumerate(docs):
        print(f"Document {i+1}")
        print("-" * 70)
        print("content:", doc.page_content[:80] + "...")
        print("\nMetadata:")
        print(json.dumps(doc.metadata, indent=2))
        print("\n")
```


1. **if I or you wonder what is `enumerate` used for?**

   enumerate gives you a Counter alongside the item.
   
   Without enumerate:
   ```
   for doc in docs:
        print(doc)
        
   # You know the doc, but you don't know which number it is.
   ```

   With enumerate:
   ```
   for i, doc in enumerate(docs):
       print(f"Document {i+1}: {doc}")
    # Output: Document 1: ..., Document 2: ...
    ```
    
    **When to use**?

   Whenever you need to display a number, track an index, or label items (like "doc 1", "doc 2") just like in our code as well.


2. `print("content:", doc.page_content[:80] + "...")`,  What does [:80] mean?

   It's called python `slicing`

   1. It takes a slice of the string from the Start up to (but not including) index 80.
  
      **In simple words** first 79 strings of the document *including*
      spaces and chars
      
   2. **why use it**? - Because our document is longer it will be pain to print the whole content in your console, for a preview purpose you use slicing.
  
3. `print(json.dumps(doc.metadata, indent=2))`

   1. `json.dumps`: Converts the Python dictionary (`metadata`) into a JSON string.
   2. `indent=2`: This is purely for visual formatting. It tells Python to add 2 spaces of indentation to make it look like a nested list.
   3. Without `indent`: `{'source':'a','tags':['x','y']}` In one line harder to understand and read, makes it look less sorted.
   4. With `indent=2`:

      ```
      {
      "source": "a",
      "tags": [
      "x",
      "y"
       ]
      }
      ```
# part 3
```
splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
        )

        split_doc = splitter.split_documents(docs)
        print(f"split {len(docs)} documents into {len(split_doc)}")
```
This part split the `docs` and print it's length along with loaded docs length.

# part 4
```
for i,doc in enumerate(split_doc[:3]):
            print(f"chunk {i+1}")
            print(f"content : {doc.page_content}")
            print(f"Source : {doc.metadata.get("source")}")
            print(f"category : {doc.metadata.get("category")}")
            print(f"Tags : {doc.metadata.get("tags")}")
            print()
```

1. `for i,doc in enumerate(split_doc[:3]):` - ** What does `split_doc[:3]` do?

   Again this is python *slicing*
   1. `split_doc` is a list of all the chunks (supposing there are more).
   2. `[:3] `tells Python: "Give me the items from the start up to (but not including) index 3."
   3. **result**?

      The loop will only run for first 3 chunks ignoring the rest,
      **why do this**? - again, for preview without printing every chunks and it's faster to prcoess only 3 items during experiments.

    **summary**:

   [:3]: Limits the loop to the first 3 items.

3. Rest is printing different objects of `metdata` using `.get(" ")`.

4. **Why is print() empty at the end**?

   `print()` with nothing inside it simply prints a blank line.

   *used when*? - you need a line break.

   1. without the empty `print()`:
      ```
      chunk 1
      content: LangChain...
      Source: langchain-intro.md
      chunk 2
      content: RAG...
      Source: rag-explained.md
      ```
   2. With the empty p`rint()`:
      ```
      chunk 1
      content: LangChain...
      Source: langchain-intro.md
      
      chunk 2
      content: RAG...
      Source: rag-explained.md
      ```
      (Create visual gap making it easier to read and understand)
    
# part 5
```
beginner_docs = [
            doc for doc in docs if doc.metadata.get("difficulty") == "beginner"
        ]
        print(f"Beginner documents : {len(beginner_docs)}")
        for doc in beginner_docs:
            print(f" -{doc.metadata.get("source")}")

        ai_docs = [
            doc for doc in docs if "ai" in doc.metadata.get("tags", [])
        ]
        print(f"\n Documents tagged 'ai' : {len(ai_docs)}")
        for doc in ai_docs:
            print(f" -{doc.metadata.get("source")}")

        print("\n Metadata is essentail for oranizing and filtering documents")
```
1. `beginner_docs = [doc for doc in docs if doc.metadata.get("difficulty") == "beginner"]`

   This creates a new list containing only the beginner docs. It is way clean and fast.

   Use the List Comprehension (the code's way) for filtering. It creates a new list you can use later.

   
   

   
