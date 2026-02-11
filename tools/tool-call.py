from langchain_core.tools import tool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

class calculatorInput(BaseModel):
    """Input schema for calculator"""
    expression : str = Field(description="The mathematical expression to evaluate e.g., '2*5', '5+4', '2-5' etc."
                            )

@tool
def calculator(expression : str) -> str:
    """A high performance tool for mathematical calculations."""

    try:
        allowed_names = {'abs': abs, 'round': round, 'min': min, 'max': max}
        result = eval(expression, {"__builtins__" : {}}, allowed_names)
        return f"The result is: {result}"
    except Exception as error:
        return f"Error evaluating expression: {error}"

def main():
    print("Tool created:", calculator.name)
    print("Description:", calculator.description)

    result = calculator.invoke({"expression": "2576 / 6446"})
    print("Result :", result)

if __name__ == "__main__":
