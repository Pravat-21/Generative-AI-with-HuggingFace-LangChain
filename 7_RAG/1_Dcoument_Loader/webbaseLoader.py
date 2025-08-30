from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)

url="https://www.amazon.in/OnePlus-Super-Silver-128GB-Storage/dp/B0D5YCYS1G/ref=asc_df_B0D5YCYS1G?mcid=f2b0de860d9f364ba1403efb2abf6927&tag=googleshopdes-21&linkCode=df0&hvadid=709962856229&hvpos=&hvnetw=g&hvrand=3230063046742302794&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061788&hvtargid=pla-2321803835669&gad_source=1&th=1"

# we are going to question something about the previous url

tamplate1=PromptTemplate(template="Give me two points description of battery of the following specification\n {text}",input_variables=['text'])

template2=PromptTemplate(template="Give me summary of the following text \n {text}",input_variables=['text'])

parser=StrOutputParser()

def output(url):
    loader=WebBaseLoader(url)
    output=loader.load()
    return output[0].page_content

runnable_fucn=RunnableLambda(output)


chain= runnable_fucn | template2 | model | parser | tamplate1 | model | parser
output=chain.invoke(url)
print(output)

