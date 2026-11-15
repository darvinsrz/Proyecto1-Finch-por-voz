from BirdBrain import Finch
from time import sleep
import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 0.5 

with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)

try:
    print("Dijiste?: " + r.recognize_vosk(audio, language="es-MX")) #type: ignore
except sr.UnknownValueError:
    print("No logré reconocer el mensaje de voz")
    print("Intenta de nuevo")