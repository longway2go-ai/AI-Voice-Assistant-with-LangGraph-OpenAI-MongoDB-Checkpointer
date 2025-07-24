# graph.py
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph.message import add_messages
from langchain_core.runnables import Runnable
from langgraph.checkpoint.mongodb import MongoDBSaver
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Annotated
import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("MONGODB_URI", "mongodb://admin1:secret1@localhost:28017")

# ---- Define state ----
class State(TypedDict):
    messages: Annotated[list, add_messages]

# ---- LLM Setup ----
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# ---- Chat function ----
def chat(state: State) -> dict:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# ---- Build Graph ----
def build_graph(checkpointer=None) -> Runnable:
    graph = StateGraph(State)
    graph.add_node("chat", chat)
    graph.set_entry_point("chat")
    graph.set_finish_point("chat")
    return graph.compile(checkpointer=checkpointer)

# ---- Create MongoDB Checkpointer ----
def get_checkpointer():
    return MongoDBSaver.from_conn_string(DB_URI)
