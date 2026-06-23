"""LangChain agent definitions for AI Judge (LangChain 1.2.18)."""

import os
from typing import List, Optional

# LangChain 1.2.x uses these imports
from langchain.agents import AgentExecutor
from langchain.agents import (
    create_tool_calling_agent,
)  # <-- important: this is the new name
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from .prompts import (
    AGENT_1_RESEARCH_PROMPT,
    AGENT_2_SOURCE_CHECKER_PROMPT,
    AGENT_3_SCORING_PROMPT,
)
from .tools import get_tools

load_dotenv()


def get_llm(model_name: Optional[str] = None) -> ChatOpenAI:
    """Returns an LLM instance (OpenAI)."""
    if model_name is None:
        model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
    return ChatOpenAI(
        model=model_name,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        temperature=0.1,
        max_tokens=4096,
    )


def create_agent(
    system_prompt: str,
    tools: List = None,
    memory=None,
    model_name: Optional[str] = None,
) -> AgentExecutor:
    """Creates a LangChain agent."""

    if tools is None:
        tools = []

    llm = get_llm(model_name)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    # LangChain 1.2.x: create_tool_calling_agent
    agent = create_tool_calling_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        max_iterations=10,
        handle_parsing_errors=True,
    )


def create_research_agent(model_name: Optional[str] = None) -> AgentExecutor:
    """Agent 1: Research."""
    return create_agent(AGENT_1_RESEARCH_PROMPT, tools=[], model_name=model_name)


def create_source_checker_agent(model_name: Optional[str] = None) -> AgentExecutor:
    """Agent 2: Source Checker."""
    tools = get_tools()
    return create_agent(
        AGENT_2_SOURCE_CHECKER_PROMPT, tools=tools, model_name=model_name
    )


def create_scoring_agent(
    model_name: Optional[str] = None, memory=None
) -> AgentExecutor:
    """Agent 3: Scoring."""
    return create_agent(
        AGENT_3_SCORING_PROMPT, tools=[], memory=memory, model_name=model_name
    )


__all__ = [
    "get_llm",
    "create_research_agent",
    "create_source_checker_agent",
    "create_scoring_agent",
]
