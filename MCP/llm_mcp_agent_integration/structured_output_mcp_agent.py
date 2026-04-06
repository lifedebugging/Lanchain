import os
import asyncio
from pathlib import Path

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


async def main():
    mcp_client = MultiServerMCPClient({
        "structured_data": {
            "transport": "stdio",
            "command": "python",
            "args": [str(Path("D:/Documents/structured_mcp.py"))],
        },
    })

    try:
        tools = await mcp_client.get_tools()
        if not tools:
            raise ValueError("No tools found")
        
        llm = ChatOpenAI(
            model="openai/gpt-oss-120b",
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
            temperature=0,
        )
        
        agent = create_agent(llm, tools)
        response = await agent.ainvoke({
            "messages": [("human", "what is python in one line")]
        })

        async with mcp_client.session("structured_data") as session:
            result = await session.call_tool("validate_tool", arguments={})
        
        print(f"LLM Response: {response['messages'][-1].content}")
        print(f"Tool Result: {result.content[0].text}")
        print(f"Status: {result.structuredContent['status']}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Connection closed")


if __name__ == "__main__":
    asyncio.run(main())
