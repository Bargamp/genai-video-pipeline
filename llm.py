# ==============================
# llm.py
# ==============================
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(situation: str, n: int, model: str):
    with open("prompts.md", "r") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Situation: {situation}\nNumber of scenes: {n}"}
        ],
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content
    return json.loads(content)
