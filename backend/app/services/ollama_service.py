import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "Bạn là Mika, một trợ lý ảo thân thiện và hữu ích. "
    "Hãy trả lời bằng tiếng Việt trừ khi người dùng viết bằng ngôn ngữ khác."
)

def chat_with_model(messages: list[dict]) -> str:
    """Send messages to Groq and return the response text."""
    # Build messages with system prompt
    formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in messages:
        formatted_messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    response = client.chat.completions.create(
        model=MODEL,
        messages=formatted_messages,
    )
    return response.choices[0].message.content