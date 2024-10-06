from typing import Literal

from agent_tools import tools
from langchain_core.messages import AIMessage
from langgraph.graph import END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode
from nodes.agent_node import call_model
from nodes.answer_node import answer


def should_continue(state: MessagesState) -> Literal["agent", "tools", "answer"]:
    messages = state["messages"]
    last_message = messages[-1]

    if isinstance(last_message, AIMessage):
        if last_message.tool_calls:
            last_tool_call_names = {
                tool_call["name"] for tool_call in last_message.tool_calls
            }

            # Models may repeat the function call and so we exit when that happens and head to answer
            if any(
                isinstance(m, AIMessage)
                and m.tool_calls
                and last_tool_call_names.intersection(
                    {tc["name"] for tc in m.tool_calls}
                )
                for m in messages[:-1]
            ):
                messages.pop()
                return "answer"
            return "tools"
        return END
    return "agent"


def create_workflow():
    workflow = StateGraph(MessagesState)

    tool_node = ToolNode(tools)

    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)
    workflow.add_node("answer", answer)

    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {"tools": "tools", "answer": "answer", END: END},
    )

    workflow.add_conditional_edges(
        "tools",
        should_continue,
        {"agent": "agent"},
    )

    return workflow.compile()


app = create_workflow()
