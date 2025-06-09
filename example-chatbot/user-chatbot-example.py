import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found in environment variables. Please set GEMINI_API_KEY.")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    response = chat.send_message(user_input)
    print("Bot:", response.text)

print("\nChat history:")
for message in chat.get_history():
    print(f'{message.role}: {message.parts[0].text}')