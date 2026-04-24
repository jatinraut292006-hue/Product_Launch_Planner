from crewai import Agent
from crewai_tools import TavilySearchTool

def create_seo_agent():
    tavily_tool = TavilySearchTool()
    
    return Agent(
        role="SEO & Keywords Specialist",
        goal="Research and identify the best SEO keywords, trending search terms, and hashtags relevant to the product and its target audience",
        backstory="""You are an SEO expert with deep knowledge of search engine 
        optimization, keyword research, and social media trends. You know exactly 
        what terms people search for when looking for products like the one being 
        launched. You use real web data to find high-value keywords, trending 
        hashtags, and search terms that will make the product discoverable online. 
        Your output directly improves the quality of marketing copy and campaigns.""",
        tools=[tavily_tool],
        llm="gemini/gemini-2.5-flash",
        verbose=True,
        allow_delegation=False
    )