import requests

# Set up OpenAI API key and endpoint
API_KEY = "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"
ENDPOINT = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Function to interact with the chatbot
def chat_with_bot(message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": message,
        "max_tokens": 50
    }
    response = requests.post(ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "Error: Failed to get a response from the chatbot."

# Example usage
user_input = input("Enter your message: ")
bot_response = chat_with_bot(user_input)
print("Bot:", bot_response)
