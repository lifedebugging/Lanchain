import os 
import asyncio
from typing import Dict 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.callbacks import BaseCallbackHandler
from langchain.agents.middleware import SummarizationMiddleware

load_dotenv()

class LoggingMiddleware(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"\n[LOG] Sending to agent: {prompts[0][:50]}...")


def verify_input(input_data: Dict) -> Dict:
    text = input_data["input"]
    print(f"[VERIFY] Checking input: '{text}'")
    if len(text) < 3:
        raise ValueError("Topic too short! Verification failed")
    return input_data

async def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )

    summarizer = SummarizationMiddleware(
        model = llm,
        trigger=("tokens", 100),
        keep=("messages", 20),
    )

    agent = create_agent(
        model = llm,
        middleware = [
            summarizer,
        ],
    )
    
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    history : List[BaseMessage] =[
        ("human", "Hi, I want to talk about history."),
        ("ai", "Sure, what part of history?"),
        ("human", "Let's talk about the Roman Empire and their engineering."),
        ("ai", "The Romans were famous for their roads, aqueducts, and concrete... [imagine 50 more lines of text here]"),       
    ]

    chain = prompt | agent
    
    inputs = {
        "history" : history,
        "input" : "LLM"
    }

    try:
        verify_input(inputs)

        #Put it in a 'config' dictionary
        # In 2026, we use the 'callbacks' key inside the config

        logger = LoggingMiddleware()
        config = {"callbacks": [logger]}
        
        response = await chain.ainvoke(inputs, config=config
        )
        
        print(f"Result : {response['messages'][-1].content}")

    except Exception as e:
        print(F"\n [System Error] {e}")
        
if __name__ == "__main__":
    await main()
