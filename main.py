# https://realpython.com/python-speech-recognition/

import speech_recognition as sr


def hello():
    print('hello')

# get audio from the microphone                                                                       
r = sr.Recognizer()                    
keyword = "hello"                                                                
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    if  r.recognize_wit(audio) == keyword:
        hello()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
