import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GROQ_API_KEY")

# Create client
client = Groq(api_key=API_KEY)


def ask_ai(prompt):
    """Send a prompt to the AI and return its response."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content