from agent_workflow import app

for message in app.stream(
    [
        (
            "system",
            """
            Include each answer below and follow the below format:
            Answer:
            {answer}
            """,
        ),
        (
            "human",
            "what is the weather in Paris? what is 3 + 3 + 3? what is 4 + 4? also what time is it in London",
        ),
    ],
    stream_mode="values",
):
    message[-1].pretty_print()
