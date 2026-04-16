# ==============================
# main.py
# ==============================
import os
import uuid
run_id = str(uuid.uuid4())
from dotenv import load_dotenv
load_dotenv()

from llm import generate_story
from image_gen import generate_image
from tts import generate_audio
from video import create_video
from storage import save_run

OUTPUT_DIR = f"output/run_{run_id}"
os.makedirs(OUTPUT_DIR, exist_ok=True)

text_model = "gpt-4.1"
image_model = "gpt-image-1"
tts_model = "gpt-4o-mini-tts"

def run_pipeline(situation: str, n: int = 4):
    story = generate_story(situation, n, text_model)

    output_data = {
        "input": situation,
        "n_scenes": n,
        "text_model": text_model,
        "image_model": image_model,
        "tts_model": tts_model,
        "scenes": []
    }

    image_files = []
    audio_files = []

    for i, scene in enumerate(story["scenes"]):
        img_path = f"{OUTPUT_DIR}/img_{i}.png"
        audio_path = f"{OUTPUT_DIR}/audio_{i}.mp3"

        print(f"Generating image {i+1}...")
        generate_image(scene["image_prompt"], img_path, image_model)

        print(f"Generating audio {i+1}...")
        generate_audio(scene["voiceover"], audio_path, tts_model)

        image_files.append(img_path)
        audio_files.append(audio_path)

        output_data["scenes"].append({
            "voiceover": scene["voiceover"],
            "image_prompt": scene["image_prompt"],
            "image_path": img_path,
            "audio_path": audio_path
        })

    print("Creating video...")
    video_path = f"{OUTPUT_DIR}/final.mp4"
    create_video(image_files, audio_files, video_path)

    output_data["video_path"] = video_path
    save_run(output_data, OUTPUT_DIR, run_id)
    
if __name__ == "__main__":
    number_of_scenes = 2
    run_pipeline(situation="Viele Junge Leute haben eine Woche lang eine tolle Zeit und viel Spaß beim Lernen, Diskutieren, Erkunden der Natur, Gesellschaftsspielen und einem Ballabend mit Tanz.", n = number_of_scenes)