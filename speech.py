# speech.py
import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os

pygame.mixer.init()

robot_ear = sr.Recognizer()
robot_ear.energy_threshold = 600     # có quạt / ồn
robot_ear.dynamic_energy_threshold = False
robot_ear.pause_threshold = 1.0
robot_ear.phrase_threshold = 0.3
robot_ear.non_speaking_duration = 0.5


def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = f"voice_{int(time.time() * 1000)}.mp3"
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    for _ in range(3):
        try:
            os.remove(filename)
            break
        except PermissionError:
            time.sleep(0.1)
