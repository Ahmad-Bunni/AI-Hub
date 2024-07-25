from agent_tools import tools
from langchain_community.chat_models import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions

llm_with_tools = OllamaFunctions(
    model="phi3", format="json", temperature=0, keep_alive="30m"
).bind_tools(tools)

llm_without_tools = ChatOllama(model="phi3", temperature=0, keep_alive="30m")
