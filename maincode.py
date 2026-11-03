from BirdBrain import Finch
from time import sleep
import speech_recognition as sr

r = sr.Recognizer()

bird = Finch()

while True: 
    
    try: 
        with sr.Microphone() as source: 
            audio = r.listen(source) 
        recognized_text = r.recognize_google(audio, language="es-MX") #type: ignore 
    except sr.UnknownValueError: 
        print("No logré reconocer el mensaje de voz")
        print("Intenta de nuevo")
        continue 

    if recognized_text == "adelante":
        print("Dijiste: ", recognized_text)
    elif recognized_text == "atrás":
        print("Dijiste: ", recognized_text)
    elif recognized_text == "izquierda":
        print("Dijiste: ", recognized_text)
    elif recognized_text == "derecha":
        print("Dijiste: ", recognized_text)
    elif recognized_text == "detente":
        print("Dijiste: ", recognized_text)
    else:
        print("Comando no reconocido")

