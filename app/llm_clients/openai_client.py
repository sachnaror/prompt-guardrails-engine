from openai import OpenAI
from app.config.settings import settings


# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate(prompt: str) -> str:
    """
    Send prompt to OpenAI model and return generated text.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Return only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=500
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError("OpenAI returned empty response")

        return content

    except Exception as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")
