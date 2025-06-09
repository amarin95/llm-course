import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "mistral:7b"

def send_message(message, history=None):
    payload = {
        "model": MODEL,
        "prompt": message,
        "stream": False,
    }
    if history:
        payload["context"] = history
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("response", ""), data.get("context", None)

def main():
    print("Chatbot Mistral (Ollama local). Type 'exit' to quit.")
    history = None
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        bot_response, history = send_message(user_input, history)
        print("Bot:", bot_response.strip())

if __name__ == "__main__":
    main()