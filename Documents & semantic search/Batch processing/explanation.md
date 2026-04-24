# Explanation

```
import os
import time

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
```
Required import libraries

```
embeddings = HuggingFaceEmbeddings(
    model= "all-MiniLM-L6-v2"
)
```
The embedding used is `HuggingFaceEmbeddings` and the model used for it is `all-MiniLM-L6-v2` our lil buddy.


```
print(" method 1 : good ol'batch embedding with embed_documents()")
    start_time = time.time()
    batch_embeddings = embeddings.embed_documents(texts)
    batch_time = time.time() - start_time
```

This is how we create embeddings previously so we were doing batch processing after all.

well in any case we are using `time` module to get current time `time.time()` 

and then embedding our document with `.embed_documents` and the content is a list of `(texts)`.

To show case how long it took to create the embedding we are subtracting current time with time right before embedding document

hence  `batch_time = time.time() - start_time`.

`print(f" Created {len(batch_embeddings)} embeddings in {batch_time:.2f}`

Here we printing how much time it took to create the embeddings in batch and if you don't know `batch_time:.2f` is about format specifier used to display floating point number like time in our case rounded to exactly two decimal places so `.2f` upto 2-floating point.


```
print("Method 2 : Individual embedding 'string-by-string' with embed_query()")
    start_time = time.time()
    individual_embeddings = []
    for text in texts:
        embedding = embeddings.embed_query(text)
        individual_embeddings.append(embedding)
    individual_time = time.time() - start_time

    print(f" Created {len(individual_embeddings)} embeddings in {individual_time:.2f}s\n")
```
This is method two, here's line by line explanation:
1. `start_time` getting current time before **individual embedding**.
2. creating a `individual_embeddings = []` empty list.
3. here we are looping over our texts which is a `list` of `string`.

   so it will loop over each string and create embeddings using `embeddings.embed_query(texts)` store it in `embedding`.

   then it will add those embeddings created into `individual_embeddings` the empty list using `individual_embeddings.append(embedding)`
   
5. we are printing the `individual_time` basically the current time - time before starting the embedding it will give us the time it took
   to create the `individual embeddings` that is the whole `for` loop.
6. And we are printing the time it took to create the length of `individual_embeddings`

```
if individual_time > batch_time:
        speedup = individual_time / batch_time
        print(f"\n Batch processing is {speedup:.1f}x faster")
    else:
        print(f"\n NOte: For small batches, performance may be similar")
```
This is where we are compairing the time for **individual embedding** and **batch embedding**

if `individual_time` is more than `batch_time` then,

divide the individual_time and batch_time and store the total time in `speedup`

this will tell you how fast is `batch_time` compare to `individual_time`.

if not then we are printing an excuse that **performance maybe be similar for small batches or docments**.


End.
   
