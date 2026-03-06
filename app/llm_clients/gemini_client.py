import google.generativeai as genai
from app.config.settings import settings


# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)


# Initialize model
model = genai.GenerativeModel("gemini-1.5-pro")


def generate(prompt: str) -> str:
    """
    Sends prompt to Gemini and returns the generated text.
    """

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0,
                "max_output_tokens": 500
            }
        )

        if not response.text:
            raise ValueError("Gemini returned empty response")

        return response.text

    except Exception as e:
        raise RuntimeError(f"Gemini API error: {str(e)}")
