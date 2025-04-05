Magic Hologram 🪞✨
A personalized assisstant that listens, talks (via OpenAI), and plays video in the background — in Persian (Farsi)!

Features
Persian Speech Recognition (Google Cloud)

GPT-powered Conversations (OpenAI)

Video Playback (MoviePy + Pygame)

Easily customizable personality via config.py

Setup
Clone this repo

Install requirements:

nginx
Copy
Edit
pip install -r requirements.txt
Add your Google Cloud credentials:

Create credentials.json from Google Cloud Speech-to-Text

Set env variable:

arduino
Copy
Edit
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json
Add your OpenAI API key:

arduino
Copy
Edit
export OPENAI_API_KEY=your_openai_key
Place your video as input.mp4 in the project folder.

Run it!
nginx
Copy
Edit
python magic_mirror.py
Customize Personality
Edit config.py:

python
Copy
Edit
SYSTEM_PROMPT = "شما یک آینه جادویی باحال هستید که..."
