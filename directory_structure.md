├── prompt-guardrails-engine/
│   ├── API_DOCUMENTATION.md
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── README.md
│   ├── docker-compose.yml
│   ├── .env.example
│   ├── app/
│   │   └── main.py
│   │   ├── routers/
│   │   │   └── prompt_router.py
│   │   ├── config/
│   │   │   └── settings.py
│   │   ├── utils/
│   │   │   ├── latency_timer.py
│   │   │   └── json_parser.py
│   │   ├── schemas/
│   │   │   ├── request_schema.py
│   │   │   └── response_schema.py
│   │   ├── rate_limit/
│   │   │   └── limiter.py
│   │   ├── prompts/
│   │   │   └── prompt_templates.py
│   │   ├── caching/
│   │   │   └── redis_cache.py
│   │   ├── logging/
│   │   │   └── logger.py
│   │   ├── services/
│   │   │   ├── guardrails_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── prompt_service.py
│   │   │   └── retry_service.py
│   │   ├── llm_clients/
│   │   │   ├── bedrock_client.py
│   │   │   ├── openai_client.py
│   │   │   ├── gemini_client.py
│   │   │   └── claude_client.py
│   │   ├── token_tracking/
│   │   │   └── token_counter.py
│   ├── tests/
│   │   ├── test_guardrails.py
│   │   └── test_prompt_api.py
│   ├── docs/
│   │   └── API.md
│   ├── scripts/
│   │   └── run_server.sh
