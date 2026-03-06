from pydantic import BaseModel, Field


class ClaimResponse(BaseModel):
    """
    Expected structured output from the LLM.
    """

    claim_type: str = Field(
        ...,
        description="Type of insurance claim"
    )

    risk_score: float = Field(
        ...,
        description="Risk score between 0 and 1"
    )

    explanation: str = Field(
        ...,
        description="Explanation of the classification"
    )
