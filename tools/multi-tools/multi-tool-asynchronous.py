from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pydantic import BaseModel , Field
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

class CalculatorInput(BaseModel):
    expression : str = Field(description="Math expression")

class SearchInput(BaseModel):
    query : str = Field(description="Search query")

class WeatherInput(BaseModel):
    city : str = Field(description="city name")

@tool(args_schema=CalculatorInput)
async def calculator(expression : str) -> str:
    """A high performance calculator to do basic math"""
    await asyncio.sleep(1)
    return str(eval(expression, #eval() is a Python function that takes a string and executes it as Python code.
                    #In this tool, the AI might pass the string "15 * 4". eval turns that string into the math operation 15 * 4 and gives you the answer.
                    {__builtins__ :{}}, ## 2. Restrict access: Remove dangerous system functions (like 'open' or 'import')
                    {}, # 3. Isolate scope: Provide an empty dictionary so no local variables can be accessed
                   ))

@tool(args_schema=SearchInput)
async def search(query : str) -> str:
    """Search for factual information"""
    await asyncio.sleep(1)
    return f"Result of the {query} : "

@tool(args_schema=WeatherInput)
async def get_weather(city : str) -> str:
    """Get current weather for a city"""
    await asyncio.sleep(1)
    return f"Weather in {city} : 72 degree, sunny"

async def main():
    llm = ChatOpenAI(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0
    )

    model_with_tools = llm.bind_tools([calculator, search, get_weather])

    queries = [
        "what is 353*464-353, use calculator tool to solve?",
        "what is the capital of France?, use search tool to answer",
        "what's the weather in Tokyo?, use get_weather tool to answer",
    ]

    tasks = []

    for query in queries:
        response = model_with_tools.invoke(query)
        if response.tool_calls:
            print(f"Query : {query}")
            print(f" Tool : {response.tool_calls[0]['name']}")
            tool_call = response.tool_calls[0]
            selected_tools = {
                "calculator" : calculator,   #Key: String Name   -> Value: Real Function
                "search" : search,
                "get_weather" : get_weather
            }[tool_call["name"]] #At the very end, we use square brackets [] to look up a key in that dictionary.
            task = selected_tools.ainvoke(tool_call['args'])
            tasks.append(task)

    result = await asyncio.gather(*tasks)

    for res in result:
        print(res)

if __name__ == "__main__":
    await main()
        
