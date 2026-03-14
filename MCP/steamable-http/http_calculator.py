from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-calculator")

@mcp.tool()
def calculate(expression : str) -> str:
    """ A high performance mathematical calculations.
    Args : 
    expression : Math expression to evaludate, e.g., '2+2', '2-2' etc.
    Returns:
    The result of the calculation."""
    
    result = eval(expression, {"__builtins__" : {}}, {})
    return str(result)


#Running with HTTP transport
mcp.run(transport = "streamable-http")

    
    
    
