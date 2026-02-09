from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field, field_validator
from dotenv import load_dotenv

load_dotenv()

class Personalinfo(BaseModel):
    name : str = Field(description="the name of the person")
    
    age : int

    @field_validator("age")
    def age_range(cls, age):
        if age < 18 or age > 25:
            raise ValueError("Age must be realistic")
        return age
    
    
    gender : str = Field(description="guess the age of the person")
    tone : str = Field(description="tone of the person talking to")

class Car(BaseModel):
    car : str = Field(description="try to guess the car that person might like assuming user is in India.")
    food : str = Field(description="food they might like make sure it's realistic assuming the user is Indian.")

def main():
    llm = ChatOpenAI(
      model=os.getenv("AI_MODEL"),
      base_url=os.getenv("AI_ENDPOINT"),
      api_key=os.getenv("AI_API_KEY"),
    )

    #strucutre output
    structured_llm = llm.with_structured_output(Personalinfo)  
    structured_llm1 = llm.with_structured_output(Car)
    
    

    text = input()
    
    response = structured_llm.invoke(text)
    

    #Accessing field

    print(f"Name : {response.name}")
    print(f"Age : {response.age}")
    print(f"gender : {response.gender}")
    print(f"tone : {response.tone}")

    

    response1 = structured_llm1.invoke(text)

    print (f"car : {response1.car}")
    print(f"food : {response1.food}")




    
if __name__ == "__main__":
    main()
