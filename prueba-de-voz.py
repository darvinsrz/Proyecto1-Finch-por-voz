import speech_recognition as sr

r = sr.Recognizer()

while True: #prueba para revisar si los comandos de voz funcionan
    with sr.Microphone() as source: #inicializa el microfno y lo guarda en source
        audio = r.listen(source) #utiliza listen para escuchar al microfono y guardar el audio en la variable audio (todavia no es texto, es un objeto de tipo AudioData)
    recognized_text = r.recognize_google(audio, language="es-MX") #type: ignore este si convierte el AudioData a str al español de México
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
