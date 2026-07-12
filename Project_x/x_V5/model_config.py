
from langchain_openai import ChatOpenAI
from tools_handling import tool_call
from dataclasses import dataclass
from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()


#model configuration

#Enum
class ModelTier(Enum):
    fast = "Fast"
    fallback = "Fallback"
    smart = "Smart"
    
    
@dataclass
class ModelConfig:
    model_name: str
    temperature: float
    max_tokens: int = 4096
    
MODEL_MAP = {
    ModelTier.fast: ModelConfig(
        model_name= "llama-3.3-70b-versatile",
        temperature= 0.6,
        max_tokens=4096
        
    ),
    ModelTier.smart: ModelConfig(
        model_name= "openai/gpt-oss-120b",
        temperature= 1.0,
        max_tokens=4096
    )
}

# def get_tools():
#     global  catched_tools
#     if catched_tools is None:
#         catched_tools = tool_call()
#     return catched_tools
    


def log_routing_decision(decision: dict) -> ModelConfig:
    """
    Routing stats and returns model config
    """
    category = decision.get("category", "UNKNOWN")
    confidence = decision.get("confidence", 0.0)
    model_tier_str = decision.get("model", "Fast")
    tools = decision.get("tool", None)
    
    try:
        tier = ModelTier(model_tier_str)
    except ValueError:
        raise ValueError(f"unkown model tier '{model_tier_str}' for intent '{category}'")
    
    config = MODEL_MAP[tier]
    
    print(f"-----[Routing Decision]-----")
    print(f"Intent detected : {category}")
    print(f"Confidence      : {confidence}")
    print(f"Model tier      : {tier.value}")
    print(f"Model ID        : {config.model_name}")
    print(f"Tools           : {tools}")
    
    return tier

def endpoint(config):
    llm = ChatOpenAI(
        model=config.model_name,
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=config.temperature
    )
    return llm
