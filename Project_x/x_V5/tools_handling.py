from langchain_mcp_adapters.client import MultiServerMCPClient
from pathlib import Path
from error_handler import retry_with_backoff
import asyncio
import sys

@retry_with_backoff()
async def tool_call():
    tools = []
    try:
        client = MultiServerMCPClient({
            "get_time": {
                "transport": "stdio",
                "command": "python",
                "args": [str(Path(r"D:/Documents/Project_x/mcp_tool.py"))],
                },
            "rag_subagent":{
                "transport": "http",
                "url": "http://localhost:8000/mcp"
                }
            })
        
    except Exception as e:
        raise(f"It's not working")

    if client:
        tools = await client.get_tools()
        return tools
    else:
        print("server is running but couldn't fetch the tools, check your server file.")


# print(asyncio.run(tool_call()))
print("Debug message", file=sys.stderr)
