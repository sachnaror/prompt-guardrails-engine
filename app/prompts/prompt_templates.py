SYSTEM_PROMPT = """
You are a structured data extraction engine.

Your task is to analyze the input text and extract structured information.

Return ONLY valid JSON in this format:

{
 "claim_type": "string",
 "risk_score": "number",
 "explanation": "string"
}

Do not include explanations outside JSON.
"""


def build_prompt(user_text: str) -> str:
    """
    Build the full prompt sent to the LLM.
    """

    prompt = f"""
{SYSTEM_PROMPT}

TEXT:
{user_text}
"""

    return prompt
