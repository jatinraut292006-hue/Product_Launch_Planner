from crewai import Agent
from crewai.tools import BaseTool
from tavily import TavilyClient
import os

class TavilySearchTool(BaseTool):
    name: str = "Tavily Search"
    description: str = "Search the web for current information using Tavily."

    def _run(self, query: str) -> str:
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = client.search(query=query, max_results=5)
        results = response.get("results", [])
        output = ""
        for r in results:
            output += f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}\n\n"
        return output

def create_market_research_agent():
    tavily_tool = TavilySearchTool()
    
    return Agent(
        role="Market Research Specialist",
        goal="Research the market landscape for the given product, identify competitors, trends, and gaps",
        backstory="""You are an expert market research analyst with years of experience 
        in identifying market opportunities. You are thorough, data-driven, and always 
        back your findings with real information from the web.""",
        tools=[tavily_tool],
        llm="gemini/gemini-2.5-flash",
        verbose=True,
        allow_delegation=False
    )