# ==============================
# video.py
# ==============================
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(image_files, audio_files, output="output.mp4"):
    clips = []

    for img, audio in zip(image_files, audio_files):
        audio_clip = AudioFileClip(audio)
        duration = audio_clip.duration

        clip = ImageClip(img).set_duration(duration)
        clip = clip.set_audio(audio_clip)

        # simple zoom effect
        clip = clip.resize(lambda t: 1 + 0.05 * t)

        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")
    final_video.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )