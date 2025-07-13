import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(prompt="🎤 Listening..."):
    with sr.Microphone() as source:
        print(prompt)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"Heard: {text}")
        return text
    except sr.UnknownValueError:
        print("❗ I didn't catch that.")
        return ""
    except sr.RequestError:
        print("❗ API unavailable.")
        return ""

def main():
    print("🤖 Jarvis is running.")
    print("Say 'hey jarvis' to wake me. Say 'stop' or 'exit' anytime to quit.")

    while True:
        text = listen("🎤 Listening for wake word or exit...")

        if "stop" in text or "exit" in text:
            print("👋 Goodbye!")
            break

        if "hey jarvis" in text:
            print("✅ Wake word detected!")
            while True:
                command = listen("🎤 Waiting for your command...")

                if "stop" in command or "exit" in command:
                    print("👋 Goodbye!")
                    return

                if command.strip() == "":
                    print("❗ Didn't catch command. Listening again...")
                    continue

                # Do something with command here
                print(f"✅ Executing command: {command}")

                # After one command, go back to wake word listening
                break

if __name__ == "__main__":
    main()

