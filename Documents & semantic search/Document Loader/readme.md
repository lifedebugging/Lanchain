# Document Loaders

`Data loaders are used to load different formats of data before splitting them, that's it.`

**Technically** :

     Document loaders in LangChain are components that load documents from various sources, 
     such as PDFs, Word files, and web pages, into a standardized format called Document objects.

**Why document loader wanted in `AI` anyway?**

Because Ai only knows one language - plain text. your data can be textfiles, pdfs, websites, json/csv and more. 
document loaders handle the complexity of reading different formatats. 
it's job is to rip out the meaining bearing text to whatever format and hand it forward. 

<img width="1536" height="769" alt="image" src="https://github.com/user-attachments/assets/409d16d9-cc11-4e92-bc23-2bc227d8079e" />

# Document loaders integrations

Documents loaders provide a standard interface for reading data from different sources into LC document format. This insures data can be handlesd consistently regardless of the source.

All document loaders implement the BaseLoader interface.

## Interface

**Each document loader may define its own parameters, but they share a common API:**

1. load() – Loads all documents at once.
2. lazy_load() – Streams documents lazily, useful for large datasets.


