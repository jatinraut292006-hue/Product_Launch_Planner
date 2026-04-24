from crewai import Agent
from crewai_tools import TavilySearchTool

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