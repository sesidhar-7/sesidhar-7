import pyttsx3

import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)              #print(voices[1])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe ():
    hour = int(datetime.datetime.now().hour)

    if hour <=0 and hour<=12:
        speak("Good Morning,Bunny")
    elif hour >=12 and hour<=18:
        speak("Good Afternoon,Bunny")
    else :
        speak("Good Evening , Bunny")    

    speak(" i am excited tell me, what is our next challenge? ")    
