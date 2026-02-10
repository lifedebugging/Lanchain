from langchain_openai import ChatOpenAI
from pydantic import BaseModel , Field
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

class structured_outputs(BaseModel):
    name : str = Field(description="""
    Name of the user, fix typos and spelling mistakes and remove blank spaces for eg: @ -> a, $ -> s, etc..
    Return only the name,
    Does not include words after name""")
    age : int = Field(description="age of the user, always convert it to integer")
    occupation : str = Field(description="The user's job. Normalize the occupation  to a standard professional title")

async def process_request(text, structured_llm):
    result = await structured_llm.ainvoke(f"extract personal information from : {text}")
    return result
    
async def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0
     )
    
    structured_llm = llm.with_structured_output(structured_outputs)

    messy_inputs = [
    "name is s @m and i m twenty my occupation lets say i kill for government",
    "call me J0hn, im th1rty five n i sell stuff for a living",
    "uhh hi im alice i think im 29?? i help doctors at the hospital",
    "Age: 40. Name: Mike Ross. Job: Lawyer.",
    "my name is d@vid 22 years old and i write python code all day",
    "they call me Neo i am ancient like 500 years old and i save the world from matrices",
    "nm is robert im 55 nd i fix cars",
    "Name: Bøb. Age: 45. Job: Builder ",
    "hello there my name is elizabeth but call me liz im 34 and work in marketing",
    "Joe, 25, Chef."
    ]

    print(f"Sending : {len(messy_inputs)} requests")

    tasks = [process_request(text, structured_llm) for text in messy_inputs]

    results = await asyncio.gather(*tasks)
    for i, res in enumerate(results):
        print(f"{i+1}. Name = {res.name} | Age = {res.age} | Occupation = {res.occupation}")
    
    print(f"===========End===============")  
    
if __name__ == "__main__":
    await main()

