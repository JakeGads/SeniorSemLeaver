# https://realpython.com/python-speech-recognition/

from PyDictionary import PyDictionary # pulls from the openword.net dict, not to be confused with Py-Dictionary which is a different package
import speech_recognition as sr # googles open source Mic reading toolset
import psutil # allows the access of powershell on all available platforms (not windows exclusive)
import os # allows for you to kill from process ID's
from tqdm import tqdm # loading bars for `for` loops

quitable_programs =  ['zoom', 'Microsoft Teams']

def get_processes(process:str = 'zoom'): 
    """
    returns a list of all currently running process with the current name
    """
    return [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if process in p.info['name']]

def get_keywords(word: str) -> list:
    """
    generates synonyms based on a singular keyword
    """
    def get_synonyms(base_word:str):
        """
        returns an dict object containing pertaint information
        """
        # makes the connection to the open dictionary
        conn = PyDictionary(base_word)
        
        # Downloads if base word is a singular word
        if base_word.count(' ') == 0:    
            return conn.getSynonyms() 
            
        # if it doesn't return a defaulted word of 0 (in the same data structure)
        return [{base_word: ['0']}]
    
    # adds the word to the base of terms
    terms = [word]
    
    # gets and appends the words from the first iteration
    for i in get_synonyms(word)[0][word]:
        terms.append(i)

    temp = []
    for i in tqdm(range(len(terms))):
        temp.extend(get_synonyms(terms[i])[0][terms[i]]) # appends to the terms's terms to a temp  
        
    terms.extend(temp) # writes temp back to terms (avoided an infinite loop scenario here)
    
    
    # loops through and removes single 
    for i in terms:
        if terms.count(i) == 1:
            del terms[terms.index(i)]
    
    
    # removes all of the 0s from the set
    for i in range(terms.count('0')):
        try:
            del terms[terms.index('0')]
        except :
            break
    
    # removes doubles, casts as a list and returns
    return list(set(terms))

    



def kill_process(process:str = 'zoom'):
    for i in get_processes(process):
        print(f"killing {i['name']}:{i['pid']}")
        os.system(f'kill {i["pid"]}')
        return True
    return False

def farwell():
    print('bye')
    # kills processes
    for i in quitable_programs:
        # if it finds a process it returns true, else it will move to the next iter
        while(kill_process(i)):
            print(i)       




# get audio from the microphone                                                                       
keywords = get_keywords('leave')
r = sr.Recognizer()                    

# async read
with sr.Microphone() as source:                                                                       
    print("In Queue:")                                                                                   
    audio = r.listen(source)   


try:
    # tests google if the spoken word is in the keywords list
    if r.recognize_google(audio) in keywords:
        farwell() # quits files
except sr.UnknownValueError:
    # for when sr fails to connect to a mic
    print("Could not understand audio")
except sr.RequestError as e:
    # for when it can't be passed up
    print("Could not request results; {0}".format(e))
