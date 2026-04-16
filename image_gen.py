# ==============================
# image_gen.py
# ==============================
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(prompt: str, filename: str, model: str):
    result = client.images.generate(
        model=model,
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json

    with open(filename, "wb") as f:
        import base64
        f.write(base64.b64decode(image_base64))

