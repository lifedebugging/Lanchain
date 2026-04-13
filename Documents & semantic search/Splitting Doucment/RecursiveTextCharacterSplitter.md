# working of RecursiveCharacterTextSplitter
Note : The working is explained using [`text_splitting.py`](text_splitting.py)

Splitting text work in few steps:

1. step - `import RecursiveCharacterTextSplitter from langchain_text_splitters`
   
   why `RecursiveCharacterTextsplitter`?
   
   Because for most use cases, start with the RecursiveCharacterTextSplitter. It provides a solid balance between keeping context intact and managing
   chunk size. This default strategy works well out of the box, and you should only consider adjusting it if you need to fine-tune performance for your
   specific application.
2. step - loading document
   ```
    with open(r"D:\Downloads\sample_text.txt", encoding='utf-8') as f:
    long_document = f.read()
    print(f"Original text length : {len(long_document)} characters\n")
    
    ```
    Here I ran into an error explained below:

   My sample_text.txt contain 10 chapters packed with:
   1. Classic Lorem Ipsum (multiple rounds)
   2. A brief history of the universe
   3. Pangrams covering every letter of the alphabet
   4. Fake sales data in a table
   5. Multilingual "Hello, World!" greetings
   6. A short poem
   7. Fake API/error responses for devs
   8. A vocabulary word list
   9. Closing remarks
   
   Cause : wide variety of characters.

   Error : UnicodeDecodeError: 'charmap' codec can't decode byte X in position Y: character maps to <undefined>

   Solution : Use `open('file_name', encoding='utf-8')`

   *refrence* : https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character

   # Continue :
   ```
   text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap = 30,
    length_function=len,
    is_separator_regex=True,
    )
    ```
    **Parameters** set above for `RecursiveCharacterSplitter`:
   1. `chunk_size:` : It's a **target**.
      
      It says - *Try your best to keep chunks under 200, but don't cut a word in half just to obey the limit*
      
   2. `chunk_overlap:` size `30` in my script means *the last 30 characters of chunk 1 repeat at the start of chunk 2*
   3. `length_function:` This is a interesting one, to understand what is `length_function` first lets' know:
      
      *why does `length_function` even exist?
  
      Because "size" isn't always **characters**.
  
      **The problem it solves** :
  
      You set `chunk_size=200` - but **200 of what exactly**?
  
      ```
      # To Python's len():
      len("hello world")  # 11 characters
      
      # To an LLM:
      "hello world"  # ≈ 2-3 tokens
      ```
      **LLMs don't think in characters — they think in tokens.**
  
      And embedding models has a *token limit*, not a character limit. So,
  
      ```
      chunk_size=200, length_function=len
      → "give me chunks of 200 characters"
      
      chunk_size=200, length_function=token_counter  
      → "give me chunks of 200 tokens"        ← what the LLM actually cares about
      ```
      **Note**:
  
      
      1. If you don't define `length_function` params, default is `characters`,
          so `ength_function=len` is just being **explicit** about what's already defualt.

      2. You can also define `your_own_function` for `length_function`.
     
3. step - **creating chunks**
   ```
   text = text_splitter.create_documents([long_document])
   print(f" Splitted into {len(text)} chunks\n")
   print('-' * 80)
   ```
   `create_documents` create the chunk out of **long_document**,
   and I am printing the `len(text)` which tell me how many chunks are there.

Rest is I m just printing each chunk using `for` loop and printing final observation.

   
  
      
# Note :
When you convert the document into **chunks** :

The **chunks** becomes a **list of Documents**, not a single Document.

Notice how we did : ``text = text_splitter.create_documents([long_document])``

Here, `text` is a **list of Documents**.

```
text = text_splitter.create_documents([long_document])
# text = [Document(...), Document(...), Document(...), ...]
#          ^ index 0       ^ index 1       ^ index 2
```
      
**Error** : I tried to print `len(text.page_content)` and the error appeared ``AttributeError: 'list' object has no attribute 'page_content'``

Solution : You can't call `.page_content` on the whole list - you have to **get inside it first**:

```
# ❌ This fails — asking the list, not a document
text.page_content

# ✅ This works — pick one document first
text[0].page_content   # first chunk
text[1].page_content   # second chunk

# ✅ Or loop through all
for doc in text:
    print(doc.page_content)
```
We did the third one.


# Splitting text from languages without word boundaries  

Some writing systems do not have word boundaries, for example Chinese, Japanese, and Thai. Just like `Multilingual` chapter in my 

      
   
    
    

   



   
    
   
   
   
