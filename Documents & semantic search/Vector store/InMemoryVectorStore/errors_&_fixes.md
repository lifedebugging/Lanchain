Errors

No text splitting — entire file was one chunk, every query returned the same document.

`AttributeError: 'str' object has no attribute 'page_content'` — passed raw string to from_documents.

`page_content="docs"` — string literal instead of variable.

Document defined inside with block, out of scope of` main()`.

`TypeError: 'tuple' object has no attribute 'page_content'` — passed single Document instead of a list.

Fixes

Used `RecursiveCharacterTextSplitter`.

Wrapped string with`Document(page_content=docs, metadata={})`.

Removed quotes — `page_content=docs`.

Moved `Document` creation inside `main()`.

Wrapped in `[]`.
