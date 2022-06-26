import subprocess
from googletrans import Translator
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes

import ctypes
import time

import shutil

from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome/exe"))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")
    while True:
        assname = ("Give me a name")
        speak("I am your Assistant")

        speak(assname)
        x=takeCommand()
        if x!=None:
            speak(x)
            speak("Thanks for the name. I love it")
            break


def username():
    while True:
        speak("What should i call you sir")
        name = takeCommand()
        speak(name)
        if name!=None:
            speak(name)
            break
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, Sir")



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return None

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    # clear()
    # wishMe()
    # username()
    translator = Translator()
    while True:

        #query = takeCommand().lower()
        text='How are you'
        text_to_translate = translator.translate(text,src='en',dest='bn')
        print(text_to_translate)
        speak(text_to_translate)

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")


        elif 'google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "path"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))


        elif 'time' in query:

            time = datetime.datetime.now().strftime('%I:%M %p')

            speak('Current time is ' + time)




        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Dhrubo")

        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by None")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by user ")



        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            while True:
                speak("What will be the file name sir?")
                file=takeCommand()

                if file!=None:
                    break
            file = str(file) + '.txt'
            speak("What should i write, sir")
            note = takeCommand()
            file1 = open(file, 'w')
            file1.write(note)


        elif "show note" in query:
            while True:
                speak("What will be the file name sir?")
                file=takeCommand()

                if file!=None:
                    break
            file = str(file) + '.txt'

            speak("Showing Notes")
            file1 = open(file, "r")
            print(file1.read())
            speak(file1.read(6))
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("Go and study")




