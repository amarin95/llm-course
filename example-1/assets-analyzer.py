import os
from PIL import Image
# Before using this install Pillow with `pip install Pillow`
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found in environment variables. Please set GEMINI_API_KEY.")

client = genai.Client(api_key=api_key)

image = Image.open("example-1/assets/violin.jpg")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, "Tell me about this instrument"]
)
print(response.text)