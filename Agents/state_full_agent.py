from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

class CalInput(BaseModel):
    expression : str = Field(description="Input value")


@tool(args_schema=CalInput)
def calculator(expression : str) -> str:
    """An high performance basic math calculator"""
    return str(eval(expression, { __builtins__ : {}},{}))

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )
    
    agent = create_agent(
        model = llm,
        tools = [calculator],
        system_prompt="You are a helpful math assistant, print output in plain text with question",
    )

    history = [HumanMessage(content ="what is 25*56?")]
    # First Invoke
    response = agent.invoke({
        "messages" : history
    })
    # Grab the Agent's reply (an AIMessage object) and ADD it to history
    # This keeps the conversation going
    
    history.append(response["messages"][-1])  #add agent answer's to history
    #[-1]: Python's special syntax for "The Last Item." 
    #This line grabs the most recent message (the Agent's answer) from the history
    
    print(f"Agent: {response["messages"][-1].content}")

    # 4. Add the NEW user question to history
    follow_up = "What was the result I just calculated?"
    history.append(follow_up)

    #Invoke with the FULL, CLEAN history
    response2 = agent.invoke({
        "messages" : history
    })
    
    print(f"Agent: {response2["messages"][-1].content}")

if __name__ == "__main__":
    main()
