# ==============================
# tts.py
# ==============================
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_audio(text: str, filename: str, model: str):
    response = client.audio.speech.create(
        model=model,
        voice="alloy",
        input=text
    )

    with open(filename, "wb") as f:
        f.write(response.content)