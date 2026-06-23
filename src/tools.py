"""Tools for agents (Web Search, URL, Current Date)."""

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools import BaseTool
from langchain_community.document_loaders import WebBaseLoader
from datetime import datetime
import os


class CurrentDateTool(BaseTool):
    name: str = "current_date"
    description: str = "Returns the current date YYYY-MM-DD."

    def _run(self, query: str = "") -> str:
        return datetime.now().strftime("%Y-%m-%d")

    async def _arun(self, query: str = "") -> str:
        return self._run(query)


class URLReaderTool(BaseTool):
    name: str = "url_reader"
    description: str = "Reads content from a URL."

    def _run(self, url: str) -> str:
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            return docs[0].page_content[:1000] if docs else "Failed to read."
        except Exception as e:
            return f"Error: {e}"

    async def _arun(self, url: str) -> str:
        return self._run(url)


def get_search_tool():
    if os.getenv("TAVILY_API_KEY"):
        return TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"), max_results=5)
    else:
        return DuckDuckGoSearchResults()


def get_tools():
    return [get_search_tool(), URLReaderTool(), CurrentDateTool()]


__all__ = ["get_tools", "CurrentDateTool", "URLReaderTool"]
