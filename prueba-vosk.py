from BirdBrain import Finch
from time import sleep
import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            audio = r.listen(source) 
        resultado = r.recognize_vosk(audio) #type: ignore #ya no especpifico el lenguaje porque el modelo de vosk instalado ya es para español
    except sr.UnknownValueError:
        print("Intenta de Nuevo")
        continue
    print("Dijiste: ", resultado.lower())
    if resultado == "alto":
        break