import os
from dotenv import load_dotenv
import speech_recognition as sr
from .graph import graph  # Correct relative import

load_dotenv(override=True)

messages = []

def main():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        mic.pause_threshold = 2

        while True:
            print("🎙️ Speak something.....")
            audio = mic.listen(source)
            print("🧠 Processing audio... (Speech-to-Text)")
            try:
                text = mic.recognize_google(audio)
                print("✅ You said:", text)
            except sr.UnknownValueError:
                print("❌ Could not understand audio.")
                continue
            except sr.RequestError as e:
                print(f"❌ Could not request results; {e}")
                continue

            # ✅ Pass the transcribed text, not audio
            messages.append({"role": "user", "content": text})

            for event in graph.stream({"messages": messages}, stream_mode="values"):
                if "messages" in event:
                    last_msg = event["messages"][-1]
                    messages.append({"role": "assistant", "content": last_msg.content})
                    last_msg.pretty_print()

if __name__ == "__main__":
    main()