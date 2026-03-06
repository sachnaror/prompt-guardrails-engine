from fastapi import FastAPI
from app.routers.prompt_router import router as prompt_router
from app.config.settings import settings

app = FastAPI(
    title="Prompt Guardrails Engine",
    description="LLM microservice with prompt guardrails and structured outputs",
    version="1.0.0"
)

# Register API routes
app.include_router(prompt_router)

# Health check endpoint
@app.get("/")
def root():
    return {
        "message": "Prompt Guardrails Engine running",
        "environment": settings.APP_ENV
    }
