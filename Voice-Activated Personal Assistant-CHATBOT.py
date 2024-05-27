import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male voice, 1 for female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def process_query(query):
    query = query.lower()

    if 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'play music' in query:
        music_dir = r"C:\MUSIC"  # Specify the path to your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))  # Change this to play a random song if needed
    elif 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results for this query, please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("No results found on Wikipedia for this query.")
    else:
        speak("I am not sure how to help with that. Please try again.")

if __name__ == "__main__":
    speak("How can I help you?")
    while True:
        query = take_command()
        if query != "None":
            process_query(query)
