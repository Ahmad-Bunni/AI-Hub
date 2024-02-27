from llama_index.llms import ChatMessage, TogetherLLM

llm = TogetherLLM(
    model="openchat/openchat-3.5-1210",
)
messages = [
    ChatMessage(role="system", content="You are a helpful assistant"),
    ChatMessage(role="user", content=""),
]

resp = llm.stream_chat(messages)

for r in resp:
    print(r.delta, end="")
