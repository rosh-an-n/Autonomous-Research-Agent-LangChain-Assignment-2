"""ReAct-based Autonomous Research Agent using LangChain."""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

from tools.web_search import web_search_tool
from tools.knowledge_tool import wikipedia_tool

load_dotenv()


REACT_PROMPT_TEMPLATE = """You are an expert research agent. Your job is to thoroughly research a given topic using the available tools and produce a comprehensive research summary.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

IMPORTANT GUIDELINES:
1. Use the web_search tool to find current, real-world information, recent developments, statistics, and examples.
2. Use the wikipedia tool to gather background knowledge, definitions, historical context, and foundational information.
3. Make multiple searches with different queries to gather diverse perspectives.
4. Always verify information from multiple sources when possible.
5. Structure your final answer with clear sections covering: Introduction, Key Findings, Challenges, Future Scope, and Conclusion.

Begin!

Question: {input}
Thought: {agent_scratchpad}"""


def create_research_agent() -> AgentExecutor:
    """Create and configure the ReAct research agent."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found. "
            "Please set it in your .env file. "
            "Copy .env.example to .env and add your key."
        )

    llm = ChatOpenAI(
        model="google/gemini-2.0-flash-001",
        openai_api_key=api_key,
        openai_api_base=base_url,
        temperature=0.3,
        max_tokens=4096,
        default_headers={
            "HTTP-Referer": "https://github.com/autonomous-research-agent",
            "X-Title": "Autonomous Research Agent",
        },
    )

    tools = [web_search_tool, wikipedia_tool]

    prompt = PromptTemplate(
        input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
        template=REACT_PROMPT_TEMPLATE,
    )

    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=15,
        max_execution_time=300,
        return_intermediate_steps=False,
    )

    return agent_executor


def research_topic(topic: str) -> str:
    """Run the research agent on a given topic and return the raw output."""
    agent_executor = create_research_agent()

    print(f"\n{'='*60}")
    print(f"  Researching: {topic}")
    print(f"{'='*60}\n")

    result = agent_executor.invoke({"input": topic})

    return result.get("output", "No research output generated.")
