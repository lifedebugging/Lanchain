from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()

class Address(BaseModel):
    street : str = Field(description="street address")
    city : str = Field(description="Name of the city")
    country : str = Field(description="Name of the country")

class Company(BaseModel):
    """Company information with nested address"""
    name : str = Field(description="Company's name")
    industry : Literal["Technologia", "Finance", "Healthcare", "Retail", "other"] = Field(description="Industry sector")
    employee_count : int = Field(description="Number of emplyees")
    headquarters : Address = Field(description="Company headquarter's location")
    is_public : bool = Field(description="Whether teh company is publicily traded")

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0
     )

    structured_llm = llm.with_structured_output(Company)

    text = """
     Microsoft Corporation is a technology giant headquartered in Redmond, Washington, USA.
    The company has approximately 220,000 employees worldwide and is publicly traded on NASDAQ.
    """

    result = structured_llm.invoke(f"Extract company's information from : {text}")

    print(f"Company : {result.name}")
    print(f"Industry : {result.industry}")
    print(f"Employees_count : {result.employee_count}")
    print(f"Location : {result.headquarters.street}, {result.headquarters.city}, {result.headquarters.country}")
    print(f"Public : {result.is_public}")

if __name__ == "__main__":
    main()

