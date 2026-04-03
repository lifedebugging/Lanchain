from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )

    agent = create_agent(
        model = llm,
        middleware= [
            SummarizationMiddleware(
            model = llm,
            trigger = ("tokens",300),
            keep=("messages", 1),
        ),
                    ],
        system_prompt= "you are a helpful assistant"
    )

    query = input("Ask your Question :" )
    response = agent.invoke({
        "messages" : [HumanMessage(content=query)]
    })

    last_message = response["messages"][-1]
    print(f"Agent : {last_message}")

if __name__ == "__main__":
    main()
