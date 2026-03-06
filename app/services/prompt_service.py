def build_prompt(user_text: str) -> str:
    """
    Build the structured prompt that forces the LLM
    to return valid JSON.
    """

    system_instruction = """
You are a structured data extraction engine.

Extract information from the input text.

Return ONLY valid JSON with the following fields:

{
 "claim_type": "string",
 "risk_score": "number",
 "explanation": "string"
}
"""

    prompt = f"""
{system_instruction}

TEXT:
{user_text}
"""

    return prompt
