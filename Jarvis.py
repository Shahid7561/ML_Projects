# Desktop Assistant

import pyttsx3
import speech_recognition as sr 
import datetime
from datetime import date
import time
import wikipedia
import webbrowser
import os
import requests
import pyjokes
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    This Function Wishes According To The Time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'am Jarvis Sir, Tell Me How May I Help You")

def takeCommand():
    '''
    It takes Microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)

        print("Say That Again Please...")
        return "None"
    return query


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic of tasks

        if 'wikipedia' in query:
            speak("Searching in Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According To Wikipedia..")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open ml playlist' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9ai6fAMHp-acBmJONT7Y4BSG")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
            
        elif 'open github' in query:
            webbrowser.open("https://github.com/")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'the date' in query:
            strDate = date.today()
            speak(f"Sir, today is {strDate}")
            print(strDate)
            
        elif 'open code' in query:
            codePath = "C:\\Users\\SHAHID\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'the headline in hindi' in query:
            webbrowser.open("https://www.divyabhaskar.co.in/")

        elif 'the headline in english' in query:
            webbrowser.open("https://timesofindia.indiatimes.com/")

        elif 'weather' in query:
            search = "temperature in ahmedabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            print(f"Current {search} is {temp}")

        elif 'open ubuntu' in query:
            uPath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(uPath)

        elif 'who are you' in query:
            speak("I'am Jarvis Sir,I'am an AI Virtual Assistance,Which Was Made By Shahid Memon In 2021")
            
        elif 'stop' in query:
            exit(0)
            
        elif 'turn off pc' in query:
            shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
            if shutdown == 'no':
                 exit()
            else:
                os.system("shutdown /s /t 1")

        elif 'set timer' in query:
            timer = int(input("Enter How Many Second For Timer: "))
            countdown(timer)
            
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())