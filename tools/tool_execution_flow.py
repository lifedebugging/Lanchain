from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

class WeatherInput(BaseModel):
    city : str = Field(description="City name")

class WeatherOutput(BaseModel):
    
    temperature : str = Field(description="Fetch Temperature of the city knowing that it's Feburary month, always use measurment after the temperature °C")

@tool(args_schema=WeatherInput)
def get_weather(city : str) -> str:
    """Get current weather for a city"""
    temps = {"seattle": 6, "Paris": 13}
    temp = temps.get(city, 6)
    return f"Current temperature in {city} : {temp}°C"

def main():
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0
    )

    model_with_tools = llm.bind_tools([get_weather])

    Query = input("enter city : ")
    
    response1 = model_with_tools.invoke(Query)
    print("step 1 - tool call:", response1.tool_calls[0])

    #tool_call is a Dictionary (or Object) that acts as a container holding three pieces of information together.
    #tool_call = {
    #'name': 'get_weather',         # 1. The function name
    #'args': {'city': 'London'},    # 2. The input data
    #'id': 'fc_2b3423bd...',        # 3. The unique ID
    #'type': 'tool_call'}

    tool_call = response1.tool_calls[0]
    tool_result = get_weather.invoke(tool_call["args"])
    print("step 2 - Tool result:", tool_result)

    structured_output = llm.with_structured_output(WeatherOutput)
    
    # We need to construct a list of messages representing the conversation so far.
    messages = [
        HumanMessage(content=Query),
        response1,
        ToolMessage(content=tool_result, tool_call_id=tool_call["id"]),
        #You are telling LangChain: "This text result ('6°C') belongs to the request with ID 'call_abc123'."
    ]
     

    final_response = structured_output.invoke(messages)
    

    print(f"Final Response : Weather in {Query} is  {final_response.temperature}")

if __name__ == "__main__":
    main()

        
    
#response1.tool_calls           # The List (The Shelf)
       ↓
#response1.tool_calls[0]        # The First Dictionary (The Folder)
       ↓
#response1.tool_calls[0]["name"] # The String "get_weather" (The Paper inside)
