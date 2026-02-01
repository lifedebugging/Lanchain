from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()



def main():
    template = ChatPromptTemplate. from_messages([
        ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("human", "{text}"),
    ])

    llm = ChatOpenAI(
        model="model_name,
        api_key=os.getenv("YOUR_API_KEY"),
        base_url="END_POINT",
    )

    chain = template | llm

    result1 = chain.invoke({
        "input_language": "English",
        "output_language" : "French",
        "text" : "Hello, how are you?",
    })

    print("french:", result1.content)

    result2 = chain.invoke({
        "input_language" : "English",
        "output_language" : "Russian",
        "text" : "Hello, how are you",
    })

    print("Russian:", result2.content)

if __name__ == "__main__":
    main()
