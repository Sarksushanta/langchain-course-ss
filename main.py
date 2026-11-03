from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searcbes over the internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """    

    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(temperature=0, model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello Langchain !!!")
    result = agent.invoke({"messages": HumanMessage(content="What is the output of the India NZ T20 match today 01 Nov 2026 ?")})
    print(result)

    
if __name__ == "__main__":
    main()