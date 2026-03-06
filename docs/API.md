
# Prompt Guardrails Engine – API Documentation

This document describes the API endpoints exposed by the Prompt Guardrails Engine.

The service receives text input, sends it to an LLM (OpenAI, Claude, Gemini, or Bedrock),
validates the response with guardrails, and returns structured JSON.

---

## Base URL

http://localhost:8000

Interactive API docs:
http://localhost:8000/docs

---

## POST /generate

Processes input text and returns validated structured JSON.

### Request

Headers:
Content-Type: application/json

Body:

{
  "text": "Customer filed a vehicle damage claim worth 2000 dollars"
}

### Response

{
  "claim_type": "vehicle_damage",
  "risk_score": 0.21,
  "explanation": "Vehicle damage claim detected"
}

---

## Execution Flow

Client Request
→ FastAPI Endpoint
→ Validation
→ Rate Limiter
→ Redis Cache
→ Prompt Builder
→ LLM Provider Router
→ Model (OpenAI / Claude / Gemini / Bedrock)
→ Guardrails Validation
→ Retry
→ Structured JSON Response

---

## Supported Providers

Configured using `.env`

LLM_PROVIDER=openai
LLM_PROVIDER=claude
LLM_PROVIDER=gemini
LLM_PROVIDER=bedrock

