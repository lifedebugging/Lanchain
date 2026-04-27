# nltk

    pip install nltk

```
import nltk
nltk.download("punkt_tab")
```

# OpenAIEmbeddings 

Head to [plateform.openai.com](https://platform.openai.com/home) to sign up to OpenAI and generate an API key. Once you’ve done this set the OPENAI_API_KEY environment variable:

```
import getpass
import os

if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
```

# Chroma DB

     pip install -qU langchain-chroma

# BM25 integration

     pip install -qU  rank_bm25
