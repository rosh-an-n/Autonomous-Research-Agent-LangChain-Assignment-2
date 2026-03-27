"""Wikipedia Knowledge Tool for the Autonomous Research Agent."""

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain.tools import Tool


def _wikipedia_wrapper(query: str) -> str:
    """Query Wikipedia and return a summary with related content."""
    try:
        api_wrapper = WikipediaAPIWrapper(
            top_k_results=3,
            doc_content_chars_max=8000,
        )
        wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
        result = wiki_tool.run(query)
        if not result or result.strip() == "":
            return f"No Wikipedia article found for: {query}"
        return result
    except Exception as e:
        return f"Wikipedia lookup error: {str(e)}. Try a different search term."


wikipedia_tool = Tool(
    name="wikipedia",
    description=(
        "Search Wikipedia for encyclopedic knowledge and background information. "
        "Use this tool to get foundational context, definitions, historical background, "
        "and well-sourced factual information about a topic. "
        "Input should be a topic or concept name."
    ),
    func=_wikipedia_wrapper,
)
