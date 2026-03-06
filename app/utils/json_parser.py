import json

"""
Safely parse JSON returned from LLM responses.
Handles cases where the LLM adds extra text.
"""


def parse_json(response_text: str) -> dict:
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:

        # Attempt to extract JSON block
        start = response_text.find("{")
        end = response_text.rfind("}") + 1

        if start != -1 and end != -1:
            json_str = response_text[start:end]
            return json.loads(json_str)

        raise ValueError("Unable to parse JSON from LLM response")
