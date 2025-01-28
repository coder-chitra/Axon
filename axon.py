import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import pygame

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Function to speak the provided audio."""
    engine.say(audio)
    engine.runAndWait()

def wishMe(name):
    """Function to wish user based on the time of the day."""
    speak(f"Hi {name}!")
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Axon, your personal assistant. I am capable of performing a variety of tasks, like searching on Wikipedia, opening websites, playing music, and much more.")
    speak("How can I assist you today?")

def takeCommand():
    """Function to take command from the user via microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please say that again.")
            return "None"
        except sr.RequestError:
            speak("Sorry, there is an issue with the speech service. Please check your connection.")
            return "None"
        return query.lower()

def play_music():
    """Function to play a music file."""
    music_file = "song.mp3"  # You can dynamically get the file name here
    if os.path.exists(music_file):
        os.startfile(music_file)
    else:
        speak("Music file not found.")

def stop_music():
    """Function to stop the music."""
    pygame.mixer.music.stop()
    speak("Music stopped.")

if __name__ == "__main__":
    # Asking user for their name and wishing them
    speak("Can you please tell me your name?")
    name = takeCommand()
    if name != "None":
        wishMe(name)
    else:
        speak("I couldn't get your name, but I am here to help!")

    while True:
        query = takeCommand()

        # Execute tasks based on user query
        if 'wikipedia' in query:
            speak("Searching Wikipedia for your query...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia,")
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif 'google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif 'chat' in query:
            speak("Opening ChatGPT website...")
            webbrowser.open("https://www.chat.com")
        elif 'music' in query:
            speak("Playing music...")
            play_music()
            # if 'stop music' in query:
            #     stop_music()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{name}, the time is {strTime}")
        elif 'code' in query:
            speak("Opening Visual Studio Code...")
            os.system("code")
        elif 'notepad' in query:
            speak("Opening Notepad...")
            os.system("notepad")
        elif 'calculator' in query:
            speak("Opening Calculator...")
            os.system("calc")
        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak(f"Thanks for using me, {name}. Have a wonderful day!")
            sys.exit()  # Clean exit
