# Logic errors:

1. Returned tuple from indexing() but passed whole tuple to BM25Retriever instead of unpacking
2. Called indexing() in both if and else branches defeating the whole purpose
3. build_retrievers() called with no arguments in else block
4. ensemble_retriever returned from build_retrievers() but not captured or returned from Indexing()
5. EnsembleRetriever initialized inside the tool function — rebuilt on every query call

# Syntax/runtime errors:

1. await outside async function
2. asyncio.run(main()) return value never printed
3. response_func() not called with ()
4. Coroutine never awaited warning on ainvoke
