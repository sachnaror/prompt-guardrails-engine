import tiktoken

"""
Utility to count tokens used in prompts and responses.
Helps estimate LLM API cost.
"""

encoding = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    """
    Count tokens in a text string.
    """
    tokens = encoding.encode(text)
    return len(tokens)


def estimate_cost(token_count: int, price_per_1k_tokens: float = 0.002):
    """
    Estimate approximate LLM cost.
    """
    return (token_count / 1000) * price_per_1k_tokens
