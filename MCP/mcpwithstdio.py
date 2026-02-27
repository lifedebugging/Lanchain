import os
import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from pathlib import Path

load_dotenv()

async def main():
    client = MultiServerMCPClient({
        "localCalculator" : {   #servername
            "transport" : "stdio", #local subprocess, not http
            "command" : "python",        #Tells your computer to start the Python interpreter.
            "args" : [str(Path(__file__).parent / "servers" / "stdio_calculator_server.py")]
        }
    })

    tools = await client.get_tools()

    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
        )
    
    agent = create_agent(llm, tools)
    
    query = "calculate 2*2"
    
    response = await agent.ainvoke({"messages" : [("human", query)]})

    last_message = response["messages"][-1]

    print (f"Agent {last_message.content}")

if __name__ == "__main__":
    await main()


# This client does nothing note that it will print an error message and written in python. Thakyou.
