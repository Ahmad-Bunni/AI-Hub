from agent_tools import tool_node
from langgraph.graph import MessageGraph
from langgraph.prebuilt import tools_condition
from llms import ollama_chat


def create_workflow():
    workflow = MessageGraph()

    workflow.set_entry_point("chat")

    workflow.add_node("tools", tool_node)
    workflow.add_node("chat", ollama_chat)

    workflow.add_edge("tools", "chat")

    workflow.add_conditional_edges("chat", tools_condition)

    return workflow.compile()


app = create_workflow()
