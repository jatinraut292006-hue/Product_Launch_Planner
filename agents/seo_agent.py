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
        llm="gemini/gemini-2.5-flash-preview-04-17",
        verbose=True,
        allow_delegation=False
    )