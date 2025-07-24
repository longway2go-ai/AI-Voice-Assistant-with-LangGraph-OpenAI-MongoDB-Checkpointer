<<<<<<< HEAD
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
=======
# 🗣️ AI Voice Assistant with LangGraph, OpenAI & MongoDB Checkpointer

This project is a voice-enabled AI assistant that interacts conversationally using OpenAI's language models.  
It uses **LangGraph** for orchestration and a **MongoDB-backed checkpointer** to maintain conversation state across sessions.

---

## 📁 Folder Structure
```

├── app/
│ ├── main.py # Runs the voice assistant loop
│ └── graph.py # Defines the LangGraph with checkpointer + OpenAI logic
├── .env # For environment variables (e.g., OpenAI & MongoDB credentials)
├── requirements.txt # Python dependencies
└── README.md

```
---

## ✅ Features

- 🎤 Microphone-based voice input
- 🧠 AI-powered conversation using OpenAI
- 🕸️ LangGraph-based stateful processing
- 💾 MongoDB checkpointer to resume and track chat threads
- ♻️ Memory of past exchanges across runs using `thread_id`

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/voice-agent.git
cd voice-agent
```

## Create a virtual environment
```
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Configure your .env file
```
OPENAI_API_KEY=your_openai_api_key
MONGODB_URL=mongodb://localhost:27017  # or your MongoDB Atlas URI
```

## 🚀 Run the Assistant
python app/main.py
```
- 🟢 Voice assistant is running. Say something!
```
## Technologies Used
```
| Tool              | Purpose                                  |
| ----------------- | ---------------------------------------- |
| LangGraph         | Graph-based conversational orchestration |
| OpenAI            | LLM responses (GPT-3.5 / GPT-4)          |
| MongoDB           | Checkpointer for long-term memory        |
| SpeechRecognition | Transcribe voice to text                 |
| Python Dotenv     | Manage API credentials securely          |

```

## License
MIT License. Feel free to use, modify, and distribute this code.

## Future Plans
```
Add Text-to-Speech response
Web UI using Gradio or Streamlit
Tool-using agent with web search or calculator
```
>>>>>>> 9bc00ccbc9e2a500d0a61e4dead534f05d9251c2
