import asyncio
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum
from pydantic import BaseModel, Field

class QueryLength(Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class StrictOutput(BaseModel):
    model_type : str = Field(description="type of model"),
    tool : List = Field(description="tools being used")
    
@dataclass
class IntentResult:
    category: str
    confidence : float
    model : str
    tool : str
    source : str    
    
    
def classify_query_length(query : str) -> QueryLength:
    words = len(query.split())
    if words <= 10:
        return QueryLength.SHORT
    elif words <=50:
        return QueryLength.MEDIUM
    return QueryLength.LONG

llm_classifier = None

async def safe_llm_classifier(query : str, ctx: Any, timeout : float = 2.0) -> Optional[Dict[str, Any]]:
    try:
        return await  asyncio.wait_for(llm_classifier(query, ctx) ,timeout = timeout)
    except asyncio.TimeoutError:
        print(f"LLM classification timed out after {timeout}s for query: '{query}'")
    return None


async def resolve_intent(
    query : str,
    keyword_results : Optional[List[Dict[str, Any]]],
    semantic_results : Optional[List[Dict[str, Any]]],
    length_tier : QueryLength,
    ctx : Any
) -> IntentResult:
    
    if length_tier == QueryLength.SHORT:
        if keyword_results and keyword_results[0].get("confidence") >= 0.9:
            return _pack(keyword_results[0], "keyword")
        
        if semantic_results and semantic_results[0].get("confidence", 0.0) >= 0.0:
            return _pack(semantic_results[0], "semantic")
        
        
        #changes to be made : return to llm classifier instead.
        #if llm classifier fails return to fallback below
        #but then again is it necessary for query with short length
        return _fallback(ctx)
    
    if length_tier == QueryLength.MEDIUM:
        if semantic_results and semantic_results[0].get("confidence" , 0.0) >= 0.34:
            return _pack(semantic_results[0], "semantic")
        
        llm_result = await safe_llm_classifier(query, ctx)
        if llm_result:
            return _pack(llm_result, "llm")
        
        return _fallback(ctx)
    
    if length_tier == QueryLength.LONG:
        llm_result = await safe_llm_classifier(query, ctx, timeout=4.0)
        if llm_result:
            return _pack(llm_result, "llm")
        
        return _fallback(ctx)
    
    
def _pack(raw: Dict[str, Any], source: str) -> IntentResult:
    return IntentResult(
        category= raw.get("category", "uncategorized"),
        confidence=float(raw.get("confidence", 0.0)),
        model=raw.get("model", "unknown"),
        tool=raw.get("tool", "none"),
        source=source
    )


def _fallback(ctx: Any) -> IntentResult:
    """Guaranteed safe fallback state"""
    return IntentResult(
        category="uncategorized",
        confidence=0.0,
        model="fast",
        tool=getattr(ctx, "tools", "none"),
        source="fallback"
    )



