from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, ModelRequest
from langchain.agents.middleware.types import ModelResponse
from langchain.messages import ToolMessage
from langchain_openai import ChatOpenAI
from typing import Callable, Any
from dotenv import load_dotenv
import os

load_dotenv()

def calculator(expression : str) -> str:
    """ High performance basic math calculator"""
    #eval expects a Dictionary for the globals argument
    result = eval(expression, {__builtins__:{}},{})
    return str(result)

def search(query : str) -> str:
    """Search for factual information"""
    return f"Result of the {query} : "

#Middleware 1 : Dynamic modeel selection
#switching to complex model
class DynamicModelMiddleware(AgentMiddleware):
    def __init__(self, messages_threshold: int = 10):
        super().__init__()
        self.messages_threshold = messages_threshold

    def wrap_model_call(
        self,
        request : ModelRequest,
        handler : Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        message_count = len(request.state["messages"])
        print(f" [Middleware] Message count: {message_count}")

        #option for complex conversation (>threshold messages)
        if message_count > self.messages_threshold:
            print(" [Middleware] Switching to more capable model")
            # return handler(request.override(model = advanced_model))

        return handler(request)

# Middleware 2: Custom Error Handling
# Catches tool failures and provides helpful fallback messages
class ToolErrorMiddleware(AgentMiddleware):
    def wrap_tool_call(
        self,
        request: Any,
        handler: Callable[[Any], ToolMessage],
    ) -> ToolMessage:
        try:
            return handler(request)
        except Exception as e:
            tool_name = request.tool_call.get("name", "unknown")
            print(f"  [Middleware] Tool '{tool_name}' failed: {e}")
            # Return graceful fallback instead of crashing
            return ToolMessage(
                content=f"I encountered an error: {e}. Let me try a different approach.",
                tool_call_id=request.tool_call.get("id", ""),
            )

fast_llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
)

# Create agent with both middleware
agent = create_agent(
    model = fast_llm,
    tools=[calculator, search],
    middleware=[DynamicModelMiddleware(), ToolErrorMiddleware()]
)



        v
