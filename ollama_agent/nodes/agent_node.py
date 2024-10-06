from langchain_core.messages import SystemMessage
from llm import llm_with_tools


def call_model(state):
    messages = state["messages"]

    prompt = """
    Only use tools that are relevant to the question.
    """

    system_message = SystemMessage(content=prompt)
    messages_with_prompt = [system_message] + messages
    response = llm_with_tools.invoke(messages_with_prompt)
    return {"messages": state["messages"] + [response]}
