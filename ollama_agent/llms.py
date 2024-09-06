from agent_tools import tools
from langchain_ollama import ChatOllama

ollama_chat = ChatOllama(model="llama3.1", temperature=0).bind_tools(tools)
