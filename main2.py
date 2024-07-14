import requests
import json
import dotenv
import os

# Get API key
dotenv.load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Replace with your Claude API endpoint
claude_api_url = "https://api.claude.com/prompt"


def send_prompt_to_claude(prompt_text):
    headers = {
        "Authorization": f"Bearer {ANTHROPIC_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "prompt": prompt_text,
        "max_tokens": 100,  # Adjust as per your requirement
        "temperature": 0.7,  # Adjust as per your preference
        "top_p": 1.0,  # Adjust as per your preference
    }

    try:
        response = requests.post(claude_api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending prompt to Claude API: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    prompt = "Write a short story about a futuristic city where robots have become the dominant species."
    result = send_prompt_to_claude(prompt)

    if result:
        print("Generated text from Claude API:")
        print(result["choices"][0]["text"])
    else:
        print("Failed to generate text from Claude API.")
