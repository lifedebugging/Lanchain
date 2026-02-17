from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.messages import HumanMessage, AIMessage, ToolMessage
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os

load_dotenv()

class CalInput(BaseModel):
    expression : str = Field(description="Input value")

@tool(args_schema=CalInput)
def calculator(expression : str) -> str:
    """ High performance basic math calculator"""
    #eval expects a Dictionary for the globals argument
    result = eval(expression, {__builtins__:{}},{})
    return str(result)

@tool
def is_prime(number: int) -> str:
    """Check if a number is prime."""
    if number < 2:
        return "False"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"False (divisible by {i})"
        return "True"

def run_react_loop(query: str, tools: list, max_iterations: int = 5):
    """Manually implement the ReAct pattern."""

    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )

    tools_by_name = {t.name: t for t in tools}

    model_with_tools = llm.bind_tools(tools)

    messages = [HumanMessage(content=query)]

    for iteration in range(max_iterations):
        print(f"\n--- ITeration {iteration +1 } ---")

        #step 1: Call the model
        response = model_with_tools.invoke(messages)
        messages.append(response)

        #step 2: Cechk if there are tool calls
        if not response.tool_calls:
            print("No more tool calls - Final answer ready")
            return response.content

        #Step 3: Execture each tool call
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call['args']

            print(f"Action : {tool_name}({tool_args}")

            #execute tool
            tool_result = tools_by_name[tool_name].invoke(tool_args)
            print(f"Observation: {tool_result}")

            messages.append(
                ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])
            )

        return "Max iterations reached"

def main():
    tools = [calculator, is_prime]
    query = "Calculate 25*16 and tell me if the result is prime number or not?"
    print(f"Query : {query}")

    result = run_react_loop(query, tools)
    print(f"\n Final Answer: {result}")

if __name__ == "__main__":
    main()


    

    
    
    
     
