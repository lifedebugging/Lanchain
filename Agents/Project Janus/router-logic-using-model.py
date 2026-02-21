from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

fast_llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
)

smart_llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    temperature=0,
)

def dynamic_agent(query: str) -> str:
    """ The function to use dynamic agent"""
    print(f" User's query : {query}")

    # Decision

    router_prompt = f"""
    You are a classifier, observer the query : {query}

    If the query is basic math and factual question (greetings,facts, etc.) that does not require complex nuron activation reply : Simple
    If the query is complex that require deep reasoning or analysis such as: Complex coding question, researching about particular topic reply : Complex
    """

    decision_response = fast_llm.invoke(router_prompt)
    decision = decision_response.content.strip()

    print(f" Router Decision : {decision}")

    #Execution

    if "Complex" in decision:
        print("using smart model")
        response = smart_llm.invoke(query)

    else:
        print("using fast model")
        response = fast_llm.invoke(query)

    return response.content


#Test case 1 
print("-"*30)
result_1 = dynamic_agent("what is 2+2?")
print(f" Answer: {result_1}\n")

#Test case 2
print ("-" * 30)
result_2 = dynamic_agent("Do a thorough research about how to earn passive income in 2026 that most people are ignoring or starting up?")
print(f" Answer: {result_2}\n")


