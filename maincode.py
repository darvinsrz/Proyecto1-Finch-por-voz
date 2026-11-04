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
        bird.setBeak(0, 100, 0) #cambia el color del pico a verde para indicar que va hacia adelante
    elif recognized_text == "atrás":
        print("Comando reconocido: ", recognized_text)
        bird.setBeak(100, 0, 0) #cambia el color del pico a rojo para indicar que va hacia atrás
        bird.setMotors(-25, -25) #ambas llantas a la misma velocidad pero negativa para que retroceda
    elif recognized_text == "izquierda":
        print("Comando reconocido: ", recognized_text)
        bird.setBeak(0, 0, 100) #cambia el color del pico a azul para indicar que va hacia la izquierda
        bird.setMotors(-25, 25) #una llanta hacia atrás y otra hacia adelante para que gire a la izquierda
    elif recognized_text == "derecha":
        print("Comando reconocido: ", recognized_text)
        bird.setBeak(100, 0, 100) #cambia el color del pico a morado para indicar que va hacia la derecha
        bird.setMotors(25, -25) #una llanta hacia adelante y otra hacia atrás para que gire a la derecha
    elif recognized_text == "detente":
        print("Comando reconocido: ", recognized_text)
        bird.setBeak(0, 0, 0)
        bird.setTail("all", 0, 0, 0)
        bird.stopAll() #detiene todo
    else:
        print("Comando no reconocido")

