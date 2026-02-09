from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

# Define your output schema with Pydantic
class Person(BaseModel):
    """Schema for person information."""
    name: str = Field(description="The person's full name")
    age: int = Field(description="The person's age in years")
    occupation: str = Field(description="The person's job or profession")

def main():
    model = ChatOpenAI(
        model=os.getenv("AI_MODEL"),
        base_url=os.getenv("AI_ENDPOINT"),
        api_key=os.getenv("AI_API_KEY"),
    )

    # Create a structured output model
    structured_model = model.with_structured_output(Person)

    text = "I am Sam 20 year old doing an assassin job while managing school"

    result = structured_model.invoke(text)

    # Access typed fields directly
    print(f"Name: {result.name}")
    print(f"Age: {result.age}")
    print(f"Occupation: {result.occupation}")

if __name__ == "__main__":
    main()
