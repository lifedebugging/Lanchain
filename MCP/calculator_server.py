from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int , b : int) -> int:
    """Add two numbers"""
    return f"a+b"

@mcp.resource("greeting://{name}")
def get_greeting(name : str)-> str:
    """Get a personalized greeting"""
    return f"Hello {name}"

@mcp.prompt()
def greet_user(name : str, style : str = "friendly")-> str:
    """Generate a greeting prompt"""
    style = {
        "friendly" : "write a warm, friendly greeting",
        "formal" : "write a formal, professional greeting",
        "casual" : "write a casual, relaxed greeting",
    }
    
    return f"{styles.get(style, styles["friendly"])} for someone named"

if __name__ == "__main__":
    mcp.run(transport="stdio")
