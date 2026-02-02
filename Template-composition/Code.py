from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    #Base  template with common elements
    base_instruction = """You are a {role} assistant.
    Your Communitcation style is {style}.
    Always be helpful and casual."""

    #compose template for different use cases
    educator_template = ChatPromptTemplate.from_messages([
        ("system", base_instruction),
        ("system", "Focus on teaching concepts clearly"),
        ("human", "{question}"),
    ])

    support_template = ChatPromptTemplate.from_messages([
        ("system", base_instruction),
        ("system", "focus on providing a simple anology for the topic"),
        ("human", "{question}")

    ])

    educator_chain = educator_template | llm
    result = educator_chain.invoke({
        "role" : "A Tsundere girl and teacher",
        "style" : " Caring but denying",
        "question" : "how to self improve?"
    })

    print("Educator Response:")
    print(result.content)
          
if __name__ == "__main__":
    main()

    
