from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Request schema
class PromptRequest(BaseModel):
    text: str


# Temporary placeholder response
@router.post("/generate")
async def generate_response(request: PromptRequest):

    # Later this will call the prompt_service and LLM
    user_text = request.text

    return {
        "input_text": user_text,
        "message": "Prompt received. LLM processing will be added next."
    }
