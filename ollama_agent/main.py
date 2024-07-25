from agent_graph import app
from langchain_core.messages import HumanMessage

for messages in app.stream(
    {
        "messages": [
            HumanMessage(content="what is the weather in Bali? also what is 1 + 1?")
        ]
    },
    stream_mode="values",
):
    messages["messages"][-1].pretty_print()
