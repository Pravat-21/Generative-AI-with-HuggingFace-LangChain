from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)

template=ChatPromptTemplate([
    ('system','You are a good {domain}-expert.'),
    ('human','tell me about {topic}')
])
prompt=template.invoke({
    'domain':'cricket',
    'topic':'Jasprit Bumrah'
})

print(prompt)