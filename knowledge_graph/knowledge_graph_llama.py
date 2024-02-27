from llama_index import (
    KnowledgeGraphIndex,
    ServiceContext,
    SimpleDirectoryReader,
)
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.graph_stores import Neo4jGraphStore
from llama_index.llms import OpenAI
from llama_index.query_engine import KnowledgeGraphQueryEngine
from llama_index.storage.storage_context import StorageContext

documents = SimpleDirectoryReader("data").load_data()

llm = OpenAI(
    temperature=0.1, api_base="http://localhost:1234/v1", api_key="your_api_key"
)

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    chunk_size=512,
)


graph_store = Neo4jGraphStore(
    url="",
    username="neo4j",
    password="farm-raincoats-documents",
    database="neo4j",
)

graph_store.query(
    """
MATCH (n) DETACH DELETE n
"""
)

storage_context = StorageContext.from_defaults(graph_store=graph_store)

index = KnowledgeGraphIndex.from_documents(
    documents,
    storage_context=storage_context,
    service_context=service_context,
)

query_engine = KnowledgeGraphQueryEngine(
    storage_context=storage_context,
    service_context=service_context,
    llm=llm,
    verbose=True,
    refresh_schema=True,
)


while True:
    user_input = input("\n")
    if not user_input or user_input.lower() == "exit":
        break

    response = query_engine.query(user_input)
    print(response)
