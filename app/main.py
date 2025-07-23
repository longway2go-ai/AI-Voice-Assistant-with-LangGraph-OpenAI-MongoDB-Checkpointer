# main.py
import os
import speech_recognition as sr
from dotenv import load_dotenv
from graph import build_graph, get_checkpointer
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

# ---- Create the assistant ----
checkpointer = get_checkpointer()
graph = build_graph(checkpointer)

# ---- Conversation state ----
messages = [
    SystemMessage(content="You are a helpful and friendly AI voice assistant. Talk conversationally.")
]

def main():
    recognizer = sr.Recognizer()

    print("🟢 Voice assistant is running. Say something!")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1.5

        while True:
            print("\n🎙️ Speak...")
            audio = recognizer.listen(source)

            print("🧠 Processing speech...")
            try:
                text = recognizer.recognize_google(audio)
                print(f"✅ You said: {text}")
            except sr.UnknownValueError:
                print("❌ Couldn't understand. Try again.")
                continue
            except sr.RequestError as e:
                print(f"❌ API error: {e}")
                continue

            if text.lower() in {"stop", "exit", "quit"}:
                print("👋 Exiting.")
                break

            # Add user message
            messages.append(HumanMessage(content=text))

            # Run the graph
            config = {"configurable": {"thread_id": "voice-thread-1"}}
            for output in graph.stream({"messages": messages}, config=config, stream_mode="values"):
                if "messages" in output:
                    assistant_msg = output["messages"][-1]
                    messages.append(assistant_msg)
                    print("\n🤖 Assistant:")
                    print(assistant_msg.content)

if __name__ == "__main__":
    main()
