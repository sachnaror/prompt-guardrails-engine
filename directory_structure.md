prompt-guardrails-engine/
│
├── README.md                    # Explains what the project does, how to install, run, and test the API.
├── requirements.txt             # List of all Python dependencies needed for the project.
├── .env.example                 # Sample environment variables file (API keys, Redis URL, configs).
├── Dockerfile                   # Instructions to build a Docker container for the application.
├── docker-compose.yml           # Runs the app with supporting services like Redis using Docker.
│
├── app/
│   ├── main.py                  # Entry point that starts the FastAPI server and registers routes.
│
│   ├── config/
│   │   └── settings.py          # Loads configuration values from environment variables.
│
│   ├── routers/
│   │   └── prompt_router.py     # Defines the API endpoint (e.g., POST /generate) for prompt requests.
│
│   ├── services/
│   │   ├── prompt_service.py    # Builds and formats prompts before sending them to the LLM.
│   │   ├── llm_service.py       # Handles communication with the LLM API (OpenAI/Bedrock).
│   │   ├── guardrails_service.py# Validates LLM responses against schema and safety rules.
│   │   └── retry_service.py     # Retries LLM calls if output format or validation fails.
│
│   ├── schemas/
│   │   ├── request_schema.py    # Defines the expected structure of incoming API requests.
│   │   └── response_schema.py   # Defines the strict JSON format the LLM must return.
│
│   ├── prompts/
│   │   └── prompt_templates.py  # Stores reusable prompt templates and system instructions.
│
│   ├── caching/
│   │   └── redis_cache.py       # Implements Redis caching to avoid repeated LLM calls.
│
│   ├── rate_limit/
│   │   └── limiter.py           # Controls how many API requests a client can make per time window.
│
│   ├── token_tracking/
│   │   └── token_counter.py     # Counts tokens used by prompts and responses to estimate cost.
│
│   ├── logging/
│   │   └── logger.py            # Central logging setup for requests, responses, and errors.
│
│   └── utils/
│       ├── json_parser.py       # Cleans and safely parses JSON returned by the LLM.
│       └── latency_timer.py     # Measures response time of LLM calls and API requests.
│
├── tests/
│   ├── test_prompt_api.py       # Tests the API endpoint to ensure prompt requests work correctly.
│   └── test_guardrails.py       # Tests schema validation and guardrail logic.
│
└── scripts/
    └── run_server.sh            # Simple script to start the FastAPI server locally.
