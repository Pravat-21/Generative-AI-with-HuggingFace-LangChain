from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()



"""llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

llm_model=ChatHuggingFace(llm=llm)

res=llm_model.invoke("Describe about Rohit Sharma in 2 lines")

print(res.content)"""

