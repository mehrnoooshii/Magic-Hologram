# Magic Hologram 🦮✨

A personalized smart mirror/hologram that listens, talks (via OpenAI), and plays video in the background — in Persian (Farsi)!

---

## Features
- Persian Speech Recognition (Google Cloud)
- GPT-powered Conversations (OpenAI)
- Video Playback (MoviePy + Pygame)
- Easily customizable personality via `config.py`

---

## Setup

1. Clone this repo
2. Install requirements:
```
pip install -r requirements.txt
```

3. Add your Google Cloud credentials:
- Create `credentials.json` from Google Cloud Speech-to-Text  
- Set env variable:
```
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

4. Add your OpenAI API key:
```
export OPENAI_API_KEY=your_openai_key
```

5. Place your video as `input.mp4` in the project folder.

---

## Run it!
```
python magic_mirror.py
```

---

## Customize Personality
Edit `config.py`:
```python
SYSTEM_PROMPT = "شما یک آیینه جادویی باحال هستید که..."
```

