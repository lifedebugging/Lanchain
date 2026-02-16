from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()

class CalInput(BaseModel):
    expression : str = Field(description="Input Value")

class Weather_input(BaseModel):
    city : str = Field(description="City name")

@tool(args_schema=CalInput)
def calculator(expression : str) -> str:
    """Calculator for basic math problem"""
    return expression(eval({__builtins__ :{}}, {}))

@tool(args_schema=Weather_input)
def get_weather(city : str) -> str:
    """Get current weather of city"""
    temp = {"London" : 105, "Mumbai" : 110, "California" : 45}
    temps = temp.get(city , 100)
    return f"Current weather of {city} : {temps}°F"

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )

    agent = create_agent(
        model = llm,
        tools = [get_weather, calculator],
        system_prompt= "You are an helpful assistant, provide all output in plain text except weather"
    )

    history = [HumanMessage(content="what is 35*2 and weather in California?")]
    response = agent.invoke({
        "messages" : history
    })
    history.append(response["messages"][-1])
    print(f"Agent : {response["messages"][-1].content}")

    follow_up = HumanMessage(content="Is that hot?")
    history.append(follow_up)
    response1 = agent.invoke({
        "messages" : history
    })

    print(f"Agent:{response1["messages"][-1].content}")

if __name__ == "__main__":
    main()
