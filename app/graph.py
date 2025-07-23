# type:igonre
import os
import openai
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain.schema import SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")



class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def run_command(cmd: str):
    """
    Takes a command line prompt and executes it on the user's machine and 
    returns the output of the command.
    Example: run_command(cmd="ls") where ls is the command to list the files.
    """
    print(f"🔧 Executing Command: {cmd}")
    result = os.system(command=cmd)
    return result


tools = [run_command]

llm = init_chat_model(
    model="gpt-4o-mini", 
    model_provider="openai",
    api_key=os.getenv("OPENAI_API_KEY")
) 
llm_with_tool = llm.bind_tools(tools=[])

def chat_bot(state: State):
    system_prompt = SystemMessage(content="""
        You are an AI Coding assistant. Your job is to use available tools to help users with their technical tasks.

        You **must** use the tool `run_command` to execute any shell commands, like:
        - creating directories (`mkdir`)
        - creating files (`touch`)
        - listing files (`ls`)
        - printing text (`echo "..." > file`)
        - reading file contents (`cat`)

        You are running on a Unix-based system (macOS/Linux).

        **Important Instructions:**
        - Never give just text output if a tool can be used.
        - If a user asks to "create", "run", or "list" files, always use `run_command`.
        - Always store files in the `chat_gpt/` folder. If it doesn’t exist, create a new one.

        Examples:
        - run_command(cmd="mkdir chat_gpt")
        - run_command(cmd="echo '<html>...</html>' > chat_gpt/todo.html")

        You are not allowed to suggest code-only answers — always execute them using `run_command`.
        """)


    message = llm_with_tool.invoke([system_prompt] + state["messages"])
    return { "messages": message }

tool_node = ToolNode(tools=tools)

graph_builder = StateGraph(State)

graph_builder.add_node("chat_bot", chat_bot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START,"chat_bot")
graph_builder.add_conditional_edges("chat_bot", tools_condition)
graph_builder.add_edge("chat_bot",END)

graph = graph_builder.compile()