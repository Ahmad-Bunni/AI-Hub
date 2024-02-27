from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

prompt = ChatPromptTemplate.from_template(
    "You are an expert coder, provide readable and optimised codes for query. {query}"
)

output_parser = StrOutputParser()
model = Ollama(model="deepseek-coder:6.7b")

chain = {"query": RunnablePassthrough()} | prompt | model | output_parser


while True:
    query = input("query:")
    for chunk in chain.stream(query):
        print(chunk, end="", flush=True)
    print("\n")
