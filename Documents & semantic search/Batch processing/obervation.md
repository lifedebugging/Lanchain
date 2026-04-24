# Observation

I was thinking what does individual_embeddings and batch_embeddings look like so I went ahead and print them see for yourself down below:

print(individual_embeddings)

```
[[-0.004774206317961216, 0.00024234615557361394, 0.0437198281288147, 0.07141070812940598, 0.04632822051644325, -0.026239681988954544, -0.025860952213406563, -0.03667450323700905, -0.05128636583685875, -0.00946290884166956,...]]
```
print(batch_embeddings)
```
[[-0.004774232394993305, 0.0002423549594823271, 0.0437198206782341, 0.07141074538230896, 0.04632817208766937, -0.02623971737921238, -0.025860963389277458, -0.036674533039331436, -0.051286354660987854, -0.009462917223572731, -0.04754931852221489,]]
```

# what I understood

Embedding models are deterministic - same input always gives same output. So why are the numbers slightly different?

Well the answer to that is `embed_documents` apply different internal processing `embed_query` - some models normalize or preprocess query embeddings differently
from document embeddings. This is intentional because queries and documents can have different roles in similarity search.
