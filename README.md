# 🚀 Product Launch Planner
### AI-Powered Multi-Agent Launch Planning System

A fully deployed, end-to-end multi-agent AI system that autonomously generates a complete product launch plan from a single user input. Built with CrewAI, Gemini API, and Tavily Search.

**Live Demo:** [Product Launch Planner](https://appuctlaunchplanner-rxsnx4jrdr5bhwv7wjftxz.streamlit.app)

---

## Problem Statement

Launching a product requires synchronized market research, cross-functional planning, audience profiling, and marketing content — all happening in the right order, with the right information flowing between each step. Today, founders, product managers, and marketing teams do this manually, switching between tools, doing their own research, and writing their own content.

A simple chatbot cannot solve this. It answers one question at a time, has no memory between steps, and cannot autonomously chain tasks together. A multi-agent system is necessary because different specialized agents must handle different domains, pass outputs to each other, use real tools like web search, and work autonomously toward a unified goal.

**Who is this for:**
- **Primary** — Startup Founders who need end-to-end launch guidance with no team support
- **Secondary** — Product Managers in MNCs who need structured, research-backed plans fast
- **Tertiary** — Marketing Teams who need audience insights and messaging ready quickly

---

## Agent Pipeline

The pipeline is broken into six sequential agents. Each agent has a clear responsibility, defined inputs and outputs, and specific tools it can use.

```
User Input (Product Name, Description, Target Market)
                        ↓
              Orchestrator (CrewAI)
                        ↓
         Market Research Agent ← Tavily Search
                        ↓
         Audience Profiling Agent
                        ↓
         SEO & Keywords Agent ← Tavily Search
                        ↓
         Strategy & Roadmap Agent
                        ↓
         Marketing & Messaging Agent
                        ↓
         Advertising & Visual Agent
                        ↓
              LLM-as-Judge (Gemini)
                        ↓
         Complete Launch Plan + Quality Score
```

| # |         Agent         |      Tools    |               Output                  |
|---|          ---          |       ---     |                ---                    |
| 0 |      Orchestrator     |   All agents  |         Final compiled plan           |
| 1 |    Market Research    | Tavily Search |    Competitor overview, trends, gaps  |  
| 2 |   Audience Profiling  |      None     |   User persona, pain points, channels |
| 3 |     SEO & Keywords    | Tavily Search |    Keywords, hashtags, posting times  |
| 4 |   Strategy & Roadmap  |      None     | Phased launch roadmap with milestones |
| 5 | Marketing & Messaging |      None     |    Tagline, email, social posts       |
| 6 |  Advertising & Visual |      None     |   Visual ad concept with design specs |

---

Tech Stack

|     Component      |          Technology          |
|        ---         |             ---              |
|  Agent Framework   |            CrewAI            |
|        LLM         | Gemini 2.5 Flash (Google AI) |
|    Search Tool     |       Tavily Search API      |
|  Image Generation  | Gemini Image Generation API  |
|    LLM-as-Judge    |       Gemini 2.5 Flash       |
|      Backend       |            Python            |
|      Frontend      |           Streamlit          |
|     Deployment     |   Streamlit Community Cloud  |

---

LLM-as-Judge

After the crew generates the full launch plan, an independent Gemini model evaluates it against a 7-criteria rubric and scores it out of 70.

Evaluation Rubric:
1. Market Research Quality — competitors, trends, gaps
2. Audience Profile Quality — persona, pain points, channels
3. SEO & Keywords Quality — keywords, hashtags, trending topics
4. Strategy & Roadmap Quality — realistic plan, clear milestones
5. Marketing Content Quality — tagline, email, social posts
6. Visual Concept Quality — detailed, executable, attention-grabbing
7. Overall Coherence — unified plan, consistent messaging

The judge returns scores per criterion, a total score, an overall assessment, and suggestions for improvement.

---

Project Structure

```
product-launch-planner/
│
├── agents/
│   ├── market_research_agent.py
│   ├── audience_profiling_agent.py
│   ├── seo_agent.py
│   ├── strategy_roadmap_agent.py
│   ├── marketing_messaging_agent.py
│   └── advertising_visual_agent.py
│
├── tasks/
│   ├── research_task.py
│   ├── audience_task.py
│   ├── seo_task.py
│   ├── strategy_task.py
│   ├── marketing_task.py
│   └── visual_task.py
│
├── crew.py               # Orchestrates all agents and tasks
├── judge.py              # LLM-as-Judge evaluation
├── image_generator.py    # Marketing image generation
├── app.py                # Streamlit UI
├── requirements.txt
├── .env.example
└── .gitignore
```

---

Setup & Installation

1. Clone the repository

```bash
git clone https://github.com/24bhosalea-sketch/Product_Launch_Planner.git
cd Product_Launch_Planner
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a `.env` file in the root directory:

```
TAVILY_API_KEY=your_tavily_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API keys:
- Tavily API Key: https://tavily.com
- Gemini API Key: https://aistudio.google.com

5. Run the app

```bash
streamlit run app.py
```

---

How to Use

1. Enter your **Product Name**
2. Enter your **Product Description**
3. Enter your **Target Market**
4. Click **Generate Launch Plan**
5. Wait 2-3 minutes while all 6 agents work sequentially
6. View each agent's output in the tabbed interface
7. Click **Evaluate Launch Plan Quality** to run the LLM-as-Judge
8. Click **Generate Marketing Image** to create a visual ad

---

Deployment

The app is deployed on Streamlit Community Cloud.

For deployment, add your API keys in the Streamlit Cloud dashboard under **Settings → Secrets**:

```
TAVILY_API_KEY = "your_key_here"
GEMINI_API_KEY = "your_key_here"
```

---

Key Design Decisions

Why CrewAI over raw LLM calls?
CrewAI gives each agent a real identity — role, goal, backstory, and tools. Agents reason independently and pass structured outputs to each other. This is a genuine multi-agent system, not just a chain of prompts.

Why Gemini 2.5 Flash?
Fast, capable, and cost-effective. Each full run costs under $0.05. Supports both text generation and image generation in one API.

Why Tavily Search?
Real-time web search gives the Market Research and SEO agents access to current competitor data, market trends, and trending keywords — information that the LLM alone cannot provide.

Why Streamlit?
Rapid deployment, Python-native, and perfect for data-heavy AI applications. No frontend complexity.

---
Authors

- Achyut Bhosale [Roll No.: 19]
- Jatin Raut [Roll No.: 20]

*End Semester Project — Agentic AI*
