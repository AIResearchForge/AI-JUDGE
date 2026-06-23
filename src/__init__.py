"""AI Judge — Internet Judge (OpenAI Direct)."""

from .agents import (
    create_research_agent,
    create_source_checker_agent,
    create_scoring_agent,
)
from .tools import get_tools
from .memory import get_memory_base
from .prompts import (
    AGENT_1_RESEARCH_PROMPT,
    AGENT_2_SOURCE_CHECKER_PROMPT,
    AGENT_3_SCORING_PROMPT,
)
from .utils import (
    extract_truth_score,
    count_stars,
    calculate_stars,
    format_report,
    parse_scoring_response,
)
from .main import run_ai_judge, main

__version__ = "1.0.0"
__all__ = [
    "create_research_agent",
    "create_source_checker_agent",
    "create_scoring_agent",
    "get_tools",
    "get_memory_base",
    "AGENT_1_RESEARCH_PROMPT",
    "AGENT_2_SOURCE_CHECKER_PROMPT",
    "AGENT_3_SCORING_PROMPT",
    "extract_truth_score",
    "count_stars",
    "calculate_stars",
    "format_report",
    "parse_scoring_response",
    "run_ai_judge",
    "main",
]
