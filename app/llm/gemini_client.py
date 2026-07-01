from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


if __name__ == "__main__":
    reply = generate_response(
        "Reply with exactly: Gemini is working."
    )

    print(reply)