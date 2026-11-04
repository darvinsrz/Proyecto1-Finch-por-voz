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
        recognized_text = recognized_text.lower() #evitar conflictos con mayusculas y minusculas
    except sr.UnknownValueError: 
        print("No logré reconocer el mensaje de voz")
        print("Intenta de nuevo")
        continue 

    if recognized_text == "adelante":
        print("Comando reconocido: ", recognized_text)
        bird.setMotors(25, 25) #ambas llantas a la misma velocidad para que avance
    elif recognized_text == "atrás":
        print("Comando reconocido: ", recognized_text)
        bird.setMotors(-25, -25) #ambas llantas a la misma velocidad pero negativa para que retroceda
    elif recognized_text == "izquierda":
        print("Comando reconocido: ", recognized_text)
        bird.setMotors(-25, 25) #una llanta hacia atrás y otra hacia adelante para que gire a la izquierda
    elif recognized_text == "derecha":
        print("Comando reconocido: ", recognized_text)
        bird.setMotors(25, -25) #una llanta hacia adelante y otra hacia atrás para que gire a la derecha
    elif recognized_text == "detente":
        print("Comando reconocido: ", recognized_text)
        bird.setMotors(0, 0) #detiene ambas llantas para que el robot se detenga
    else:
        print("Comando no reconocido")

