from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

class CalculatorInput(BaseModel):
    expression: str = Field(description="Math expression")

class SearchInput(BaseModel):
    query: str = Field(description="Search query")

class WeatherInput(BaseModel):
    city: str = Field(description="City name")

@tool(args_schema=CalculatorInput)
def calculator(expression: str) -> str:
    """Perform mathematical calculations."""
    return str(eval(expression, {"__builtins__": {}}, {}))

@tool(args_schema=SearchInput)
def search(query: str) -> str:
    """Search for factual information."""
    results = {"capital of france": "Paris", "population of tokyo": "14 million"}
    return results.get(query.lower(), "No results found")

@tool(args_schema=WeatherInput)
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return f"Weather in {city}: 72°F, sunny"

def main():
    model = ChatOpenAI(
        model=os.getenv("AI_MODEL"),
        base_url=os.getenv("AI_ENDPOINT"),
        api_key=os.getenv("AI_API_KEY"),
    )

    model_with_tools = model.bind_tools([calculator, search, get_weather])

    queries = [
        "What is 125 * 8?",
        "What's the capital of France?",
        "What's the weather in Tokyo?",
    ]

    for query in queries:
        response = model_with_tools.invoke(query)
        if response.tool_calls:
            print(f"Query: {query}")
            print(f"  Tool: {response.tool_calls[0]['name']}")
            selected_tools = {
                "calculator" : calculator,   
                "search" : search,
                "get_weather" : get_weather
            }[tool_call["name"]] 
            results = selected_tools.invoke(tool_call['arg'])
            print(result)

if __name__ == "__main__":
    main()
