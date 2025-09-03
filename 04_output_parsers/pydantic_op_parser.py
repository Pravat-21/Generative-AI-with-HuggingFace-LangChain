from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)

class person(BaseModel):
    name: str=Field(description="give a name")
    age: int=Field(gt=18,description="give the age of person")
    city: str=Field(description="give me city name of the person")

parser=PydanticOutputParser(pydantic_object=person)

template=PromptTemplate(template="give me a frictional name, age & city of a{nation} person.\n {format_instruction}",
                        input_variables=['nation'],
                        partial_variables={'format_instruction':parser.get_format_instructions()}
                        )
chain=template|model|parser
result=chain.invoke({'nation':'indian'})
print(result)