from ai.ai_client import ask_ai


def summarize_notes(notes):
    prompt = f"""
You are an AI Study Assistant.

Summarize the following notes in a simple and easy-to-understand way.

Notes:
{notes}

Give:
1. Main points
2. Important definitions
3. Key takeaways
"""

    response = ask_ai(prompt)

    return response