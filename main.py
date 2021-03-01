# https://realpython.com/python-speech-recognition/

import speech_recognition as sr
import psutil
import os

quitable_programs =  ['zoom', 'Microsoft Teams']

def get_processes(process:str = 'zoom'): 
    return [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if process in p.info['name']]

def kill_process(process:str = 'zoom'):
    for i in get_processes(process):
        print(f"killing {i['name']}:{i['pid']}")
        os.system(f'kill {i["pid"]}')
        return False
    return True




def farwell():
    for i in quitable_programs:
        while(kill_process(i)):
            print(i)       


# get audio from the microphone                                                                       
r = sr.Recognizer()                    
keyword = "hello"

with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    if r.recognize_google(audio) == keyword:
        farwell()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
