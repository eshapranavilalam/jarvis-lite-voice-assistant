# JARVIS Lite - Intelligent Voice Assistant

## Overview
JARVIS Lite is a Python-based voice assistant that performs system-level tasks using speech recognition and text-to-speech technology.

It can respond to voice commands and automate simple tasks like opening websites, telling time, and launching applications.

---

## Features
- Voice-controlled interaction
- Time and date announcement
- Open Google and YouTube
- Launch Notepad
- Exit command
- Text-to-speech response

---

## Technologies Used
- Python
- SpeechRecognition
- pyttsx3
- datetime module
- webbrowser module
- os module

---

## How It Works
1. Microphone captures voice input.
2. SpeechRecognition converts voice to text.
3. Program checks the command using conditional logic.
4. Task is executed.
5. pyttsx3 converts text response to speech.

---

## How To Run

1. Install required libraries:
   pip install SpeechRecognition pyttsx3 pyaudio

2. Run the program:
   python main.py

---

## Future Improvements
- Add NLP-based intent recognition
- Add GUI interface
- Add machine learning support
- Integrate more system-level automation
