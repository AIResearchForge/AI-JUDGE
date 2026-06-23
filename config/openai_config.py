"""Configuration for direct OpenAI API."""

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def get_llm(model_name: str = None):
    """Returns an LLM instance via direct OpenAI API."""

    if model_name is None:
        model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")

    return ChatOpenAI(
        model=model_name,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        temperature=0.1,
        max_tokens=4096,
    )
