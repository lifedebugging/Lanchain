# High performance Async Data Processor

Overview 

This project is a Python-based data pipeline designed to extract structured information from unstructured text inputs.
It uses a  Large Language Models in conjunction with asynchronous programming to achieve high-throughput data processing.
The system ingests raw, messy text containing personal details, validates the output against a strict schema.

# Architecture 

The pipeline operates on a MapReduce-style logic optimized for I/O-bound tasks: 

    Ingestion: Loads raw text inputs from a local JSON list. 
    Task Dispatch: Creates a list of asynchronous coroutine tasks. 
    Concurrent Processing: asyncio.gather executes all LLM calls simultaneously. 
    Validation: The LLM response is parsed and validated against the structured_outputs Pydantic model. 
    Storage: Validated objects are serialized to dictionaries and written to disk. 
