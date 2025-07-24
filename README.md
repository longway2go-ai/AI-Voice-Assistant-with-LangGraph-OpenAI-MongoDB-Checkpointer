# 🎙️ Voice-Activated Shell Assistant with LangGraph & OpenAI

This project is a **voice-controlled command execution assistant** using:
- 🧠 OpenAI's `gpt-4o-mini`
- 🔁 LangGraph for stateful control flow
- 🗣️ `speech_recognition` for real-time voice input
- ⚙️ Tool-based Unix shell command execution (via `run_command`)

---

## 📁 Project Structure
```
.
├── app/
│ ├── main.py # Voice input, transcribes to text, triggers LangGraph
│ ├── graph.py # LangGraph StateGraph with tool nodes
│ └── init.py
├── .env # Stores environment variables
├── requirements.txt # Python dependencies
└── README.md # This file

```

---

## 🧠 What It Does

You speak into your microphone, and this AI-powered assistant:
1. Transcribes your voice into text
2. Feeds the transcription to GPT-4o-mini via LangGraph
3. Executes relevant shell commands via a secured tool interface

Example interaction:

> You say: "Make a folder and write a message to a file"  
Assistant will:
```bash
run_command(cmd="mkdir chat_gpt")
run_command(cmd="echo 'Hello from voice' > chat_gpt/message.txt")
```
## 🚀 Getting Started

### Clone the repo
```
git clone https://github.com/your-username/voice-shell-assistant.git
cd voice-shell-assistant
```
### Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Add Your .env File
```
Create a .env file in the root with:

OPENAI_API_KEY=your_openai_api_key_here
```

## 🎤 Run the App
```
python -m app.main
```