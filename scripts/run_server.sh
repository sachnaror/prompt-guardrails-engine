#!/bin/bash

echo "Starting Prompt Guardrails Engine..."

export PYTHONPATH=$(pwd)

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
