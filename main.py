import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()




def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        # Shorter ambient noise adjustment time
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        engine.say("Listening")
        engine.runAndWait()
        
        
        try:
            # Listen with a short timeout for quicker response
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""
        except sr.WaitTimeoutError:
            # Timeout error if no speech is detected within the timeout period
            return ""

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    engine.say("Searching the World Wide Web")
    engine.runAndWait()
    print(f"Opening URL: {url}")
    webbrowser.open(url)

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    wake_up_word = "wake"
    quit_word = "sleep"

    print("Program started. Say 'wake' to wake up and 'sleep' to quit.")
    engine.say("Program started. Say 'wake' to wake up and 'sleep' to quit.")
    engine.runAndWait()

    while True:
        detected_text = recognize_speech_from_mic(recognizer, microphone)
        print(f"Detected: {detected_text}")
        engine.say(f"Detected: {detected_text}")
        engine.runAndWait()

        if wake_up_word in detected_text:
            print("Wake word detected. Now listening for commands.")
            engine.say("Wake word detected. Now listening for commands.")
            engine.runAndWait()
            while True:
                command = recognize_speech_from_mic(recognizer, microphone)
                print(f"You said: {command}")

                if quit_word in command:
                    print("Quitting program.")
                    engine.say("Quitting program")
                    engine.runAndWait()
                    return
                elif command:
                    print(f"Searching for: {command}")
                    search_web(command)
                    print("Continuing to listen for new commands or 'sleep' to quit.")
                    engine.say("Continuing to listen for new commands or 'sleep' to quit.")
                    engine.runAndWait()
                else:
                    print("No command detected. Continuing to listen.")
                    engine.say("No command detected. Continuing to listen.")
                    engine.runAndWait()

if __name__ == "__main__":
    main()
