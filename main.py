# https://realpython.com/python-speech-recognition/

from pydictionary import PyDictionary # pulls from the openword.net dict, not to be confused with Py-Dictionary which is a different package
import speech_recognition as sr # googles open source Mic reading toolset
import psutil # allows the access of powershell on all available platforms (not windows exclusive)
import os # allows for you to kill from process ID's
from tqdm import tqdm # loading bars for `for` loops

quitable_programs =  ['zoom', 'Microsoft Teams'] # matches their process IDs

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
    words = get_synonyms(word)
    terms.extend(get_synonyms(word)[0][word])
    
    # removes doubles, casts as a list and returns
    return list(set(terms))

    



def kill_process(process:str = 'zoom'):
    for i in get_processes(process): # runs over all the found process
        # kills based on the pid instead of the app
        # done this way for speed for constant re-kills
        print(f"killing {i['name']}:{i['pid']}") 
        os.system(f'kill {i["pid"]}') # kills based on current
        return True # returns true incase it needs to loop
    return False

def farwell():
    print('bye')
    # kills processes
    for i in quitable_programs:
        # if it finds a process it returns true, else it will move to the next iter
        while(kill_process(i)):
            print(i)       



if __name__ == '__main__':                                                                
    # populates keywords, by file if it is found
    keywords = []
    if os.path.exists('bye.syn'):
        keywords = open('bye.syn', 'r').readlines()
    else:
        keywords = get_keywords('bye')
        with open('bye.syn', 'w+') as f:
            for i in keywords:
                f.write(i + "\n")

    # loads the spreads recognizer
    r = sr.Recognizer()                    

    # async read
    with sr.Microphone() as source:                                                                       
        print("In Queue:")                                                                                   
        audio = r.listen(source)   


    try:
        # tests google if the spoken word is in the keywords list
        if r.recognize_google(audio) in keywords: # bottle neck, this is the slowest part and why this doesn't work in general
            farwell() # quits files
    except sr.UnknownValueError:
        # for when sr fails to connect to a mic
        print("Could not understand audio")
    except sr.RequestError as e:
        # for when it can't be passed up
        print(f"Could not request results; {e}")
