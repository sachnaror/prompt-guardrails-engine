from app.services.llm_service import call_llm
from app.services.guardrails_service import validate_response


MAX_RETRIES = 3


def execute_with_retry(prompt: str):
    """
    Retry LLM calls if response validation fails.
    """

    last_error = None

    for attempt in range(MAX_RETRIES):

        try:
            raw_response = call_llm(prompt)
            validated = validate_response(raw_response)

            return validated

        except Exception as e:
            last_error = e

    raise Exception(f"LLM failed after retries: {last_error}")
