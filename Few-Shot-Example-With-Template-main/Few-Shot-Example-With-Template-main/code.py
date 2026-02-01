from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    #Teaching example
    examples = [
        {"input": "happy", "output": "😊"},
        {"input": "sad", "output": "😢"},
        {"input": "excited", "output": "🎉"},
    ]

    #Example template
    example_template = ChatPromptTemplate.from_messages([
        ("human", "{input}"),
        ("ai", "{output}"),
    ])

    #Few_shot_template
    few_shot_template = FewShotChatMessagePromptTemplate(
        example_prompt= example_template,
        examples = examples,
    )

    #Final template combining system message + examples + user input
    final_template = ChatPromptTemplate.from_messages([
        ("system", "You are an emoji translator. Convert words to emojis."),
        few_shot_template,
        ("human", "{input}"),
    ])

    chain = final_template | llm

    #For new inputs
    word = input()
    result = chain.invoke({"input": word})
    print(f"emoji for {word} -> {result.content}")

if __name__ == "__main__":
    main()

    
    
