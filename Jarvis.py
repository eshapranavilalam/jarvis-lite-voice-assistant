# ==========================================================
# ADVANCED PERSONAL AI VOICE ASSISTANT
# IIT MADRAS SUMMER INTERNSHIP PROJECT
# ==========================================================

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import os
import requests
import sys

# =========================
# INITIAL SETUP
# =========================

engine = pyttsx3.init()
engine.setProperty('rate', 170)
recognizer = sr.Recognizer()

# =========================
# SPEAK FUNCTION
# =========================

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# =========================
# LOGGING FUNCTION
# =========================

def log_command(command):
    if command.strip() != "":
        with open("assistant_log.txt", "a", encoding="utf-8") as file:
            file.write(f"{datetime.datetime.now()} : {command}\n")

# =========================
# TAKE VOICE COMMAND
# =========================

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Network issue. Please check your internet.")
        return ""

# =========================
# WEATHER FUNCTION
# =========================

def get_weather(city):
    api_key = "YOUR_OPENWEATHER_API_KEY"   # <-- REPLACE WITH YOUR REAL KEY

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 404:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The temperature in {city} is {temp} degree Celsius with {desc}.")
        else:
            speak("City not found.")

    except:
        speak("Weather service is currently unavailable.")

# =========================
# MAIN ASSISTANT FUNCTION
# =========================

def run_assistant():

    speak("Advanced assistant activated. How can I help you?")

    while True:

        command = take_command()

        if command == "":
            continue

        log_command(command)

        try:

            # Wikipedia
            if "wikipedia" in command:
                speak("Searching Wikipedia.")
                query = command.replace("wikipedia", "")
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except:
                    speak("Sorry, I could not find information.")

            # Open YouTube
            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube.")

            # Open Google
            elif "open google" in command:
                webbrowser.open("https://www.google.com")
                speak("Opening Google.")

            # Smart Search
            elif "search" in command:
                query = command.replace("search", "")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Searching for {query}")

            # Time
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")

            # Date
            elif "date" in command:
                today = datetime.date.today()
                speak(f"Today's date is {today}")

            # Joke
            elif "joke" in command:
                speak(pyjokes.get_joke())

            # Weather
            elif "weather" in command:
                speak("Please tell me the city name.")
                city = take_command()
                if city != "":
                    get_weather(city)

            # Open Notepad (Windows)
            elif "open notepad" in command:
                os.system("notepad")
                speak("Opening Notepad.")

            # Create File
            elif "create file" in command:
                speak("Tell me the file name.")
                filename = take_command()
                if filename != "":
                    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
                        file.write("File created by Advanced AI Assistant.")
                    speak("File created successfully.")

            # Exit
            elif "exit" in command or "stop" in command:
                speak("Shutting down. Goodbye.")
                sys.exit()

            # Unknown Command
            else:
                speak("That feature is not available yet, but I am learning.")

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong, but I am still running.")

# =========================
# START PROGRAM
# =========================

if __name__ == "__main__":
    run_assistant()