from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

class CalInput(BaseModel):
    expression : str = Field(description="Input value")


@tool(args_schema=CalInput)
def calculator(expression : str) -> str:
    """An high performance basic math calculator"""
    return str(eval(expression, { __builtins__ : {}},{}))

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )
    
    agent = create_agent(
        model = llm,
        tools = [calculator],
        system_prompt="You are a helpful math assistant, print output in plain text with question",
    )

    history = [HumanMessage(content ="what is 25*56?")]

    response = agent.invoke({
        "messages" : history
    })
    
    history.append(response["messages"][-1])  
    print(f"Agent: {response["messages"][-1].content}")
    
    follow_up = "What was the result I just calculated?"
    history.append(follow_up)

    response2 = agent.invoke({
        "messages" : history
    })
    
    print(f"Agent: {response2["messages"][-1].content}")

if __name__ == "__main__":
    main()
