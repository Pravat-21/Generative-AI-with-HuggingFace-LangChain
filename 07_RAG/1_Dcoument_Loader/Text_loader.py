from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

"""Suppose we are creating one application where model takes text from our directory and them give us summary of it"""

template= PromptTemplate(template="write a summary of the following poem \n {poem}",input_variables=['poem'])

loader=TextLoader(file_path="E:/CAMPUSX/GEN AI/CODE/7_RAG/1_Dcoument_Loader/cricket.txt",encoding='UTF-8')

docs=loader.load()
poem=docs[0].page_content

chain=template | model | parser
output=chain.invoke({'poem',poem})
print(output)