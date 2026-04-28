
# type annotation error
```
rank_fusion_func = ensemble_retriever.arank_fusion(
    query : str,
) -> list[Document]
```

`query: str` is also a type annotation — in a function call you just pass the value, no type.
# implentation error
```
--> 937         response = tool.invoke(call_args, config)

NotImplementedError: StructuredTool does not support sync invocation.
During task with name 'tools' and id '40d2aa7a-fe80-e334-e611-35548e7eb42b'
```
**solution** : `response = agent.ainvoke()` instead of `.invoke()` since `tool` is async

# type error
```
 111 #final response
    112 response = agent.ainvoke(
    113     {"messages" : [HumanMessage(content=query)]}
--> 117 final_response = response["messages"][-1]
    119 print(final_response.content)

TypeError: 'coroutine' object is not subscriptable
```

**solution**: `await` it:

         response = await agent.ainvoke(
    {"messages" : [HumanMessage(content=query)]}
    )

# type error 2
```
TypeError: EnsembleRetriever.arank_fusion() missing 1 required positional argument: 'run_manager'
During task with name 'tools' and id '4dc687e6-fa94-60fe-1c61-87dd6129905d'
```

`run_manager` is an internal LangChain parameter, you're not supposed to pass it manually. This means arank_fusion is not the right method to call directly.

**solution** : remove the arank_fsion`

# Ensemble error

the EnsembleRetriever being initialized inside the tool function instead of outside.

**solution** : Initialize outside the tool function.
