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

    text = "I am Sam 20 year old doing an assassin job while managing school"
    result = llm.invoke(f"Extract personal information from:{text} only print Name, age and occupation") 
    print(result.content)

if __name__ == "__main__":
    main()
