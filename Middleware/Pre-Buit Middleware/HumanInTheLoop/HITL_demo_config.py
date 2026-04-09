from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model = "openai/gpt-oss-20b",
    api_key= os.getenv("GROQ_API_KEY"),
    base_url = "https://api.groq.com/openai/v1"
)

agent = create_agent(
    model = llm,
    #tools = [write_file_tool, execute_sql_tool, read_data_tool],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file" : True, #All decisions (approve, edit, reject)
                "execute_sql" : {"allowed_decisions" : ["approve", "reject"]}, #No editing
                "read_data" : False, #Safe operation no approval needed
            },

            description_prefix = "Tool execution pending approval"
        ),
        
    ],
    checkpointer=InMemorySaver(),
)
