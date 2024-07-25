from langchain_core.messages import AIMessage, ToolMessage
from llm import llm_without_tools


def answer(state):
    messages = state["messages"]
    question = messages[0].content

    tool_responses = [
        f"{msg.name}: {msg.content}" for msg in messages if isinstance(msg, ToolMessage)
    ]

    if tool_responses:
        evaluation_prompt = f"""
        You are a helpful assistant that answers questions.

        Use the responses in your answer: {', '.join(tool_responses)}.

        Question: {question}
        
        Answer:
        """
    else:
        evaluation_prompt = f"Question: {question}"

    evaluation = llm_without_tools.invoke(evaluation_prompt)
    return {
        "messages": state["messages"] + [AIMessage(content=evaluation.content.strip())]
    }
