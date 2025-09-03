from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(template="Write down a detailed information about {topic}",
                        input_variables=['topic']
                        )

template2=PromptTemplate(template="Write down a 5 lines summary about {summary_topic}",
                        input_variables=['summary_topic']
                        )
parser=StrOutputParser()

# chain
chain= template1 | model | parser | template2 | model | parser

result= chain.invoke({'topic':'solar system'})
print(result)