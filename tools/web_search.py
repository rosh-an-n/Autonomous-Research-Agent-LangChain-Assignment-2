"""DuckDuckGo Web Search Tool for the Autonomous Research Agent."""

from ddgs import DDGS
from langchain.tools import Tool


def _search_wrapper(query: str) -> str:
    """Execute a DuckDuckGo search and return formatted results."""
    try:
        results = DDGS().text(query, max_results=5)
        if not results:
            return f"No search results found for: {query}"

        formatted = []
        for i, r in enumerate(results, 1):
            title = r.get("title", "No title")
            body = r.get("body", "No description")
            href = r.get("href", "")
            formatted.append(f"{i}. {title}\n   {body}\n   Source: {href}")

        return "\n\n".join(formatted)
    except Exception as e:
        return f"Search error: {str(e)}. Try rephrasing the query."


web_search_tool = Tool(
    name="web_search",
    description=(
        "Search the web for current information using DuckDuckGo. "
        "Use this tool to find recent news, statistics, studies, and real-world examples. "
        "Input should be a clear, specific search query string."
    ),
    func=_search_wrapper,
)
