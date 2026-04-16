# 🎬 GenAI Video Pipeline

This project is a simple end-to-end GenAI pipeline that transforms a
text situation into a fully generated short video.

It uses: - LLMs for story generation - Image generation for visual
scenes - Text-to-speech for narration - MoviePy for video assembly

------------------------------------------------------------------------

# 🧱 PROJECT STRUCTURE

    .env
    main.py
    llm.py
    image_gen.py
    tts.py
    video.py
    storage.py
    prompts.md
    output/

------------------------------------------------------------------------

# ⚙️ SETUP

## 🐍 Create Virtual Environment

### Mac

``` bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

``` bash
python -m venv venv
venv\Scripts\activate
```

------------------------------------------------------------------------

## 📦 Install Dependencies

``` bash
pip install --upgrade pip
pip install openai moviepy python-dotenv
OR
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 🔐 ENVIRONMENT VARIABLES

Create a `.env` file in the project root:

    OPENAI_API_KEY=your_api_key_here

------------------------------------------------------------------------

# 🎬 FFMPEG INSTALLATION (REQUIRED)

This project requires FFmpeg for video rendering.

## 🍏 Mac

``` bash
brew install ffmpeg
```

## 🪟 Windows

Install FFmpeg manually or via a package manager and ensure it is added
to PATH.

## 🐧 Linux

``` bash
sudo apt update
sudo apt install ffmpeg
```

------------------------------------------------------------------------

# 🚀 RUN THE PROJECT

``` bash
python main.py
```

------------------------------------------------------------------------

# 🧠 HOW IT WORKS

1.  Input text describes a situation
2.  A language model generates structured scenes:
    -   voiceover text
    -   image prompts
3.  Each scene is converted into:
    -   an image (image generation API)
    -   an audio narration (text-to-speech API)
4.  All scenes are combined into a video using MoviePy
5.  Output files are saved in the `output/` folder

------------------------------------------------------------------------

# 📁 OUTPUTS

The pipeline generates:

-   Generated images (`.png`)
-   Generated audio (`.mp3`)
-   Final video (`.mp4`)
-   Full structured run metadata (`run.json`)

------------------------------------------------------------------------

# 💡 FEATURES

-   End-to-end AI video generation from text
-   Scene-based storytelling
-   Modular architecture (easy to extend)
-   Fully reproducible JSON outputs
-   Consistent prompts for visual coherence

------------------------------------------------------------------------

# 🎓 EDUCATIONAL GOALS

This project is designed for teaching:

-   Prompt engineering for LLMs
-   Multimodal AI pipelines
-   Image + audio generation APIs
-   Video processing in Python
-   Real-world system design with AI tools

------------------------------------------------------------------------

# ⚠️ COMMON ISSUES

## ❌ API errors

→ Check `.env` file and API key

## ❌ MoviePy errors

→ Usually caused by missing or misconfigured FFmpeg

------------------------------------------------------------------------

# 📌 OPTIONAL EXTENSIONS

-   Add transitions (fade, zoom, pan)
-   Add multiple visual styles (cinematic, anime, documentary)
-   Change the GenAI models used
-   Change the voice used for tts
-   Add cost tracking per run
-   Add background music

------------------------------------------------------------------------

# 🏁 RESULT

A fully generated AI video created from a single text input using a
modular GenAI pipeline.
