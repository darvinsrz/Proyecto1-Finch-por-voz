from BirdBrain import Finch
from time import sleep
import speech_recognition as sr

bird = Finch()

r = sr.Recognizer()
r.pause_threshold = 0.4

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        recognized_text = r.recognize_vosk(audio, language="es-MX")

