import json


REQUIRED_FIELDS = [
    "claim_type",
    "risk_score",
    "explanation"
]


def validate_response(response_text: str) -> dict:
    """
    Validate that LLM response is valid JSON and
    contains required fields.
    """

    try:
        data = json.loads(response_text)
    except Exception:
        raise ValueError("LLM response is not valid JSON")

    for field in REQUIRED_FIELDS:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    return data
