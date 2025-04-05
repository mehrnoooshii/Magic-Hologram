import queue
import pygame
import numpy as np
import sounddevice as sd
from moviepy.editor import VideoFileClip
from google.cloud import speech
import openai
from pydub import AudioSegment
import signal
import sys

from config import INPUT_VIDEO_PATH, SYSTEM_PROMPT

# Initialize pygame
pygame.init()
screen = None

# Queue to store audio chunks
audio_queue = queue.Queue()
stop_streaming = False

# Initialize conversation history
conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

# Handle exit signals
def signal_handler(sig, frame):
    global stop_streaming
    stop_streaming = True
    print("Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Audio callback for sounddevice
def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

# Speech-to-text using Google Cloud Speech-to-Text
def recognize_speech():
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="fa-IR"
    )

    streaming_config = speech.StreamingRecognitionConfig(config=config, interim_results=False)

    with sd.InputStream(samplerate=16000, channels=1, callback=audio_callback):
        audio_generator = (yield_audio() for _ in range(1))
        requests = (speech.StreamingRecognizeRequest(audio_content=content) for content in audio_generator)
        responses = client.streaming_recognize(streaming_config, requests)

        for response in responses:
            for result in response.results:
                if result.is_final:
                    return result.alternatives[0].transcript

# Generator for audio chunks
def yield_audio():
    while not audio_queue.empty():
        data = audio_queue.get()
        audio = (data * 32767).astype(np.int16).tobytes()
        yield audio

# Get AI response from OpenAI
def get_ai_response(user_input):
    conversation_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    reply = response["choices"][0]["message"]["content"]
    conversation_history.append({"role": "assistant", "content": reply})

    return reply

# Play video using pygame and moviepy
def play_video():
    clip = VideoFileClip(INPUT_VIDEO_PATH)
    global screen
    screen = pygame.display.set_mode(clip.size)

    for frame in clip.iter_frames(fps=24, dtype="uint8"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        surface = pygame.surfarray.make_surface(np.rot90(frame))
        screen.blit(surface, (0, 0))
        pygame.display.update()

# Main loop
def main():
    play_video()

    while not stop_streaming:
        print("Listening...")
        user_input = recognize_speech()
        print("User said:", user_input)

        response = get_ai_response(user_input)
        print("AI:", response)

if __name__ == "__main__":
    main()
