from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_core.pydantic_v1 import BaseModel, Field


class Story(BaseModel):
    moral: str = Field(description="moral of the story")


llm = Ollama(model="mistral:instruct", temperature=0)

parser = PydanticOutputParser(pydantic_object=Story)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

query = """
"""
output = chain.invoke({"query": query})

print(output)
