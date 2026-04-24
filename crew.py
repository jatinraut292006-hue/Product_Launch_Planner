import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

from crewai import Crew, Process
from agents.market_research_agent import create_market_research_agent
from agents.audience_profiling_agent import create_audience_profiling_agent
from agents.seo_agent import create_seo_agent
from agents.strategy_roadmap_agent import create_strategy_roadmap_agent
from agents.marketing_messaging_agent import create_marketing_messaging_agent
from agents.advertising_visual_agent import create_advertising_visual_agent
from tasks.research_task import create_research_task
from tasks.audience_task import create_audience_task
from tasks.seo_task import create_seo_task
from tasks.strategy_task import create_strategy_task
from tasks.marketing_task import create_marketing_task
from tasks.visual_task import create_visual_task


def run_crew(product_name, product_description, target_market):

    market_research_agent = create_market_research_agent()
    audience_profiling_agent = create_audience_profiling_agent()
    seo_agent = create_seo_agent()
    strategy_roadmap_agent = create_strategy_roadmap_agent()
    marketing_messaging_agent = create_marketing_messaging_agent()
    advertising_visual_agent = create_advertising_visual_agent()

    research_task = create_research_task(
        market_research_agent, product_name, product_description, target_market
    )
    audience_task = create_audience_task(
        audience_profiling_agent, product_name, product_description, target_market
    )
    seo_task = create_seo_task(
        seo_agent, product_name, product_description, target_market
    )
    strategy_task = create_strategy_task(
        strategy_roadmap_agent, product_name, product_description, target_market
    )
    marketing_task = create_marketing_task(
        marketing_messaging_agent, product_name, product_description, target_market
    )
    visual_task = create_visual_task(
        advertising_visual_agent, product_name, product_description, target_market
    )

    audience_task.context = [research_task]
    seo_task.context = [research_task, audience_task]
    strategy_task.context = [research_task, audience_task, seo_task]
    marketing_task.context = [research_task, audience_task, seo_task, strategy_task]
    visual_task.context = [audience_task, marketing_task]

    crew = Crew(
        agents=[
            market_research_agent,
            audience_profiling_agent,
            seo_agent,
            strategy_roadmap_agent,
            marketing_messaging_agent,
            advertising_visual_agent,
        ],
        tasks=[
            research_task,
            audience_task,
            seo_task,
            strategy_task,
            marketing_task,
            visual_task,
        ],
        process=Process.sequential,
        verbose=True
    )

    crew.kickoff()

    full_output = ""
    for task in crew.tasks:
        full_output += f"\n\n---\n\n### {task.agent.role}\n\n"
        full_output += str(task.output)

    return full_output