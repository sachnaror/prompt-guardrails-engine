from pydantic import BaseModel, Field


class PromptRequest(BaseModel):
    """
    Schema for incoming API request.
    """

    text: str = Field(
        ...,
        description="Input text that needs structured extraction",
        example="Customer filed a vehicle damage claim worth 2000 dollars"
    )
