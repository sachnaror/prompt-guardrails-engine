"""
LLM service router.

This module selects which LLM provider to use
based on configuration in the .env file.
"""

from app.config.settings import settings

from app.llm_clients import openai_client
from app.llm_clients import claude_client
from app.llm_clients import gemini_client
from app.llm_clients import bedrock_client


def call_llm(prompt: str) -> str:
    """
    Routes the prompt to the selected LLM provider.
    """

    provider = settings.LLM_PROVIDER.lower()

    if provider == "openai":
        return openai_client.generate(prompt)

    elif provider == "claude":
        return claude_client.generate(prompt)

    elif provider == "gemini":
        return gemini_client.generate(prompt)

    elif provider == "bedrock":
        return bedrock_client.generate(prompt)

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
