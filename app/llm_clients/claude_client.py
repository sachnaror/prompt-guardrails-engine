import anthropic
from app.config.settings import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def generate(prompt: str):

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text
