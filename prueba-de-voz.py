import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source: #inicializa el microfno y lo guarda en source
    print("Di algo!")
    audio = r.listen(source) #utiliza listen para escuchar al microfono y guardar el audio en la variable audio (todavia no es texto, es un objeto de tipo AudioData)
    print(audio)
    print(type(audio))

recognized_text = r.recognize_google(audio, language="es-MX") #este si convierte el AudioData a str al español de México
print(recognized_text)

print(dir(r)) #solo para ver que metodos hay, ignorar
