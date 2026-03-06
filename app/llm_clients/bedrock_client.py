import boto3
import json
from app.config.settings import settings


# Initialize Bedrock client
client = boto3.client(
    "bedrock-runtime",
    region_name=settings.AWS_REGION
)


def generate(prompt: str) -> str:
    """
    Send prompt to AWS Bedrock model and return response text.
    """

    try:
        body = json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 500,
            "temperature": 0
        })

        response = client.invoke_model(
            modelId="anthropic.claude-v2",
            body=body,
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response["body"].read())

        completion = result.get("completion")

        if not completion:
            raise ValueError("Bedrock returned empty response")

        return completion

    except Exception as e:
        raise RuntimeError(f"Bedrock API error: {str(e)}")
