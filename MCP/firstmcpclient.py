import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

load_dotenv()

async def main():
    #context7 MCP server - provides documentation for libraries
    mcp_server_url = os.getenv("MCP_SERVER_URL", "https://mcp.context7.com/mcp")

    #create mcp client with http transport to context7
    client = MultiServerMCPClient({ 
        "context7": {         #servername
            "transport" : "streamable_http",
            "url" : mcp_server_url,
        }
    })

    try:
        #1 get all available tools form contex7
        print("fetching tools form context7 mcp server...")
        tools = await client.get_tools()

        print(f" retrieved {len(tools)} tools from context7")
        for tool in tools:
            print(f"  {tool.name}: {tool.description}")

        #2 create model
        llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
        )

        #3 create agent with MCP tools - same create_agent() pattern
        agent = create_agent(llm,tools)

        #4 use the agent to get documentation
        query = "how do i use python requests library to make HTTP get requests? get the latest documentation."
        print(f" User : {query}\n")

        response = await agent.ainvoke({"messages": [("human", query)]})
        last_message = response["messages"][-1]
        print (f" Agent : {last_message.content}\n")

    finally:
        print (" MCP client connection closed")

if __name__ == "__main__":
    await main()
