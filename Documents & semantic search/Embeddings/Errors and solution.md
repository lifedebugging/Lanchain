# **TypeError** : Embeddings.create() got an unexpected keyword argument 'temperature'
default parameter.
                    temperature was transferred to model_kwargs.
                    Please confirm that temperature is what you intended.

**solution** :
Temperature does not apply to embeddings. At all.

**let's see again what is temperature?**]

Temperature controls randomness in text generation — how creative or deterministic the model is when producing words. 
Embeddings don't generate text. They just convert text to numbers. No randomness involved, no temperature needed.

It's an OpenAIEmbeddings thing — it inherited the parameter but it doesn't use it. 
Just remove `temperature=0` from your embeddings initialization.

But also — did you switch to HuggingFace embeddings? Because if yes, temperature isn't a parameter there at all. The error suggests you're still using OpenAIEmbeddings.

# BadRequestError: Error code: 400 - {'error': {'message': "'input' : input must be a string or an array of strings", 'type': 'invalid_request_error'}}

     35 print("Creating embeddings for texts...\n")
   ---> 37 all_embeddings = embeddings.embed_documents(texts)

   **Solution** : The error is coming from Groq's API. Groq doesn't support embedding models — it only does chat/text generation. So OpenAIEmbeddings
   pointing at Groq's endpoint is failing because Groq doesn't have an embeddings endpoint.

   Switching to HuggingFace.

# ImportError: Could not import sentence_transformers python package. Please install it with `pip install sentence-transformers`.

   **Solution** :

   Well obviously, `python -m pip install sentence-transformers`

   
   
