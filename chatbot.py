# chatbot.py
import os
from config import OPENAI_API_KEY

try:
    import openai
    openai.api_key = OPENAI_API_KEY
except ImportError:
    openai = None

def get_gravlosa_reply(user_input):
    if openai is None:
        return "Error: The 'openai' package is not installed. Please run 'pip install openai' to use Gravlosa."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Gravlosa, a helpful and smart assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"
