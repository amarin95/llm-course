from google import genai
import os

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found in environment variables. Please set GEMINI_API_KEY.")

client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["How does AI work?"]
)
print(response.text)