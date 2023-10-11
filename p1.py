import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning!")  
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JArvis sir. Plese tell me how may i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  #seconds of non speaking audio before a phrase is considered complete
        audio=r.listen (source) #all are coming from speech recognition module

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, Language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="main":
    wishMe()
    while True:
        query=takeCommand().lower()
 #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
