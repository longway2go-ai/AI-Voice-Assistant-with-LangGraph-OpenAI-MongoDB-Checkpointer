# 🗣️ Conversational Voice Assistant with OpenAI + LangGraph Checkpointer

This project is a voice-enabled AI assistant that interacts conversationally using OpenAI's language models.  
It uses **LangGraph** for orchestration and a **MongoDB-backed checkpointer** to maintain conversation state across sessions.

---

## 📁 Folder Structure

├── app/
│ ├── main.py # Runs the voice assistant loop
│ └── graph.py # Defines the LangGraph with checkpointer + OpenAI logic
├── .env # For environment variables (e.g., OpenAI & MongoDB credentials)
├── requirements.txt # Python dependencies
└── README.md

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

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Configure your .env file

OPENAI_API_KEY=your_openai_api_key
MONGODB_URL=mongodb://localhost:27017  # or your MongoDB Atlas URI

## 🚀 Run the Assistant
python app/main.py
# 🟢 Voice assistant is running. Say something!
