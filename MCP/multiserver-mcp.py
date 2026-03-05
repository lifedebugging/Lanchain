import os 
import asyncio
from pathlib import Path

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

async def main():


    client = MultiServerMCPClient({
        "localcalculator" : {
            "transport" : "stdio",
            "command" : "python",
            "args" : [str(Path("D:/Documents/first_mcpserver.py"))],   #Local math server
        },
        "context7" : {
            "transport" : "streamable_http",
            "url": "https://mcp.context7.com/mcp"  #Remote docs server
            },

    })

    try: 
        print("fetching tools from all servers")
        tools = await client.get_tools()

        print(f"retrieved {len(tools)} tools from all servers")

        llm = ChatOpenAI(
                model="openai/gpt-oss-120b",
                api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1",
                temperature=0,
                )
        
        query = "calculate 335*43 and tell me what is changing that llm engineer or ai architect engineer required in 2026 given that jr llm engineer are no more required."
        print(query) 

        agent = create_agent(llm, tools)

        response = await agent.ainvoke({"messages" : [("human", query)]})

        last_messages = response["messages"][-1]

        print (f" Agent : {last_messages.content}")
        
    finally:
        print("connection close successfully")  

if __name__ == "__main__":
    asyncio.run(main())


#Note : We are using first_mcpserver.py for local math tool.


