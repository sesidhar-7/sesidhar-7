import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Ensure the correct voice ID
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Output: {audio}")  # Print the text to the console
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 2000
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Sorry, the service is down.")
        return "None"
    return query

# Main program loop
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                # Assuming takeCommand() gets user input as a string
                query = takeCommand().lower().strip()  # Convert to lowercase and remove leading/trailing spaces

                if "take rest" in query:
                    speak("Okay bunny, catch you in a while")
                    break
                elif "hello" in query:
                    speak("Hey bunny, what's up!")
                    
                elif  "I am fine" in query:
                    speak("Happy to hear that,bunny")
                    
                elif "how are you" in query:
                    speak("Super good,Bunny! What about you?")    
                    
                elif "thank you" in query:
                    speak("There's no need for thank you between friends")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia "  in query:
                    from SearchNow import searchWikipeia
                    searchWikipeia(query)

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"bunny, the time is {strTime}")

                elif " sleep" in query:
                    speak(" hurrayh ,i am going slepp  bye bye")
                    exit()



    
