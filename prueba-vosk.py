from BirdBrain import Finch
from time import sleep
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

resultado = r.recognize_vosk(audio) #type: ignore
print(resultado)
print(type(resultado))