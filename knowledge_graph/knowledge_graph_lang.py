from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import GraphCypherQAChain
from langchain.chat_models import ChatOpenAI
from langchain.graphs import Neo4jGraph

handler = StdOutCallbackHandler()

graph = Neo4jGraph(
    url="",
    username="neo4j",
    password="farm-raincoats-documents",
)

chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(
        temperature=0.1,
        openai_api_base="http://localhost:1234/v1",
        openai_api_key="not-needed",
    ),
    graph=graph,
    verbose=True,
)


result = chain.run("how many drivers are there and list their names")
print(result)
