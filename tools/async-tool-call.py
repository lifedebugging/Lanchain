# Async version
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

class calculatorInput(BaseModel):
    """Input schema for calculator"""
    expression : str = Field(description="The mathematical expression to evaluate e.g., '2*5', '5+4', '2-5' etc.")



@tool
def calculator(expression : str) -> str:
    """A high performance tool for mathematical calculations."""
    try:
        # Safety: Only allow basic math operations in eval
        allowed_names = {'abs': abs, 'round': round}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as error:
        return f"Error: {error}"

async def main():
    """Python evaluates 224*4 before it runs the code. Your list actually contains [896, 5576578453, ...].
    You need to pass Strings so the tool (or LLM) sees the math problem, not the answer.
    Fix: ["224*4", "5576578453", ...]"""
    messy_inputs = [
        
        "224*4","5576578453","676+53454","97-9966","45767/232","4354*34534","435757+67675-56764","3454*4565/567357"
    ]  

    print(f"Calculating : {len(messy_inputs)} values concurrently")

    # THE ASYNC LOOP
    # We pass a DICTIONARY {"expression": value}, NOT a prompt string
     #Tool needs: Dictionary {"expression": "2+2"}
    tasks = [calculator.ainvoke({"expression": expr}) for expr in messy_inputs]
    

    results = await asyncio.gather(*tasks)
    for i, result in enumerate(results):
        # result is just a string here because the tool returns a string
        print(f"{i+1}. The result is : {result}")


if __name__ ==  "__main__" :
    await main()


      
#If you just want to run the tool logic asynchronously (without an LLM thinking about it), 
#you do not pass a prompt. You pass the arguments directly.      
    



