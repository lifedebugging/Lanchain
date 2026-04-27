import os 
import getpass
import nltk

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from nltk.tokenize import word_tokenize

load_dotenv(override=True)


llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )

#document loader
loader = PyPDFLoader(
    file_path= r"D:\Downloads\eit-digital-artificial-intelligence-report.pdf",
    # headers= None,
    # password= None,
    mode= "single",
    extract_images= True,
    extraction_mode= "layout",
)

documents = loader.load()

#splitter
splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size= 500,
    chunk_overlap= 50,
)

splitted_documents = splitter.split_documents(documents)

#embeddings
embeddings = OpenAIEmbeddings(
    model= "text-embedding-3-large",
    api_key= os.getenv("OPENAI_API_KEY")
)

#vector store
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="D:/Downloads/",
)

#retriever
retriever = BM25Retriever.from_documents(
    splitted_documents,
    k=5,
    preprocess_func=word_tokenize,
)

#search tool
@tool
def search_docs(query: str) -> str:
    """
    "Search documentation provided for specific information about AI. 
    Use this when you need factual information from the material you've been provided.
    """
    result = retriever.invoke(query)
    
    chunks = []
    for doc in result:
        chunks.append(doc.page_content)

    return chunks
        


#agent
agent = create_agent(
    model = llm,
    tools=[search_docs],
    system_prompt=
     """ Role: You're an sub-agent with external knowledge base with context.
               You're intelligently capable to decide when to use your external knowledge base.

         Constraints: Use the following pieces of retrieved context to answer the question. 
                      If you don't know the answer, just say that you don't know.
                      Do not produce wrong answer with confidence.
                      For general questions answer without directly without using tools.

         Output_format: Precise and meaningful.
         """
)

#chain


#query
query = input()

#final response
response = agent.invoke(
    {"messages" : [HumanMessage(content=query)]}
)


final_response = response["messages"][-1]

print(final_response.content)

               


    

