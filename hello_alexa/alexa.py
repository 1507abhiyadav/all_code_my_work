from multiprocessing.connection import Listener
import speech_recognition as sr

import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id) ### for female voice
# engine.say('I am your alexa')
# engine.say('What can I do for you')
# engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("listening ............")
        voice = listener.listen(source)
        command= listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
          print(command)
          talk(command)  ### alexa repeat your voice. 
except:
    pass   
