"""
Simple MCP server for stdio Transport (Local deployment)

This server runs as a subprocess and communicates via stdio.
"""

import math
import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("stdio-calculator")

@mcp.tool()
def calculate(expression:str) -> str:
    """ A hight performance calculator using python's math module.
    Args :
         expression: Math expression to evaluate 2+2, sqrt(16), sin(pi/2)"""
    try:
        safe_namespace = {
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "pow": pow,
            # Math module functions
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "floor": math.floor,
            "ceil": math.ceil,
            "pi": math.pi,
            "e": math.e,
            
        }
        
        result = eval(expression, {__builtins__ : {}}, safe_namespace)
        return f"{expression} = {result}"
    except Exception as e:
        raise ValueError(f"Inavalid expression {e}")
    
@mcp.tool
def convert_temperature(value : float, from_unit : str, to_unit : str) -> str:
    """
    Convert temperature between calsius and Fahrenheit
    """
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == to_unit:
        return f"{value}"
    
        
