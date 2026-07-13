import os
import uvicorn


from pydantic import BaseModel

# from error_handler import retry_with_backoffs
from intent_router import normalization, keyword_intent, semantic_intent
from model_config import log_routing_decision
from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from collections.abc import AsyncIterator

from _init_ import get_ctx, lifespan, AppStateContext


# from logging_handler import setup_logging, get_logger

from dotenv import load_dotenv

load_dotenv(override=True)

# structured query
class Query(BaseModel):
    query: str
    thread_id: str 


app = FastAPI(lifespan=lifespan)

#handler
@app.post("/route")
async def handler(query: Query, 
                  ctx: AppStateContext = Depends(get_ctx),   #telling the router it's dependency
                  ):
    # StreamingResponse for streaming output
    return StreamingResponse(main(query, ctx), 
                            media_type="text/plain", 
                            )

def predict_language(text: str,k: int=1, ctx: AppStateContext = get_ctx):
        label, prob = ctx.lang_model.predict(text, k)
        return list(zip([l.replace("__label__", "") for l in label], prob))


#decision logic
def decision_logic(query : Query,  ctx: AppStateContext) -> str:
    
    
    # result = predict_language(query.query, ctx)
    normalized_query = normalization(query.query)
    keyword_results = keyword_intent(query.query)
    semantic_results = semantic_intent(query.query)
    # if result[0][0] == "en":
    #     pass
    # else:
    #     print("fallback to llm router")
        
    
    #tunnel split for keyword searching and semantic search
    if len(normalized_query.split()) <= 10:
        intent =  keyword_results          #keyword_results[0] if keyword_results else None
        
    else:
        return {"category": "SEMANTIC", "model": "Fast", "tool": ctx.tools, "confidence": 0.0}
    
    print(f"intent: {intent}")
    if intent:  
        return {
            "category" : intent[0]["category"],
            "confidence" : intent[0]["confidence"],
            "model": intent[0]["model"],
            "tool": intent[0]["tool"],
            "priority": intent[0]["priority"], 
        }
    
    else:
        return {"category": "SEMANTIC", "model": "Fast", "tool": ctx.tools, "confidence": 0.0}
        
 
async def main(query : Query,  ctx: AppStateContext) -> AsyncIterator[str]:
    decision = decision_logic(query, ctx)
    
    tier = log_routing_decision(decision)
    # for tool in tools:
    #     print(f"Tools available: {tool.name}")

    agent_call = ctx.agent_lookup[tier]
    
    async for event in agent_call.astream_events({"messages" : [("human", query.query)]},
                                                    {"configurable": {"thread_id": query.thread_id}}, 
                                                    version="v2",
                                                    ):
            
        if event["event"] == "on_chat_model_stream":
            yield event["data"]["chunk"].text
    
             
if __name__ == "__main__":
    try:
        uvicorn.run("x_v5:app", host = "127.0.0.1", port = 8001, reload= True)
    except Exception as e:
        print(f"an error occured: {e}") 
