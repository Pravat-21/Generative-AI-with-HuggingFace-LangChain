from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model1=ChatHuggingFace(llm=llm)

parser=StrOutputParser()
class Feedback(BaseModel):

    sentiment : Literal['positive','negative']=Field(description="Give me the sentiment of the feedback whether it is positive or negative")

parser_py=PydanticOutputParser(pydantic_object=Feedback)

template1=PromptTemplate(template="Generate the sentiment of the feedback \n {feedback}\n {format_instruction}",
                        input_variables=['feedback'],
                        partial_variables={'format_instruction':parser_py.get_format_instructions()}
                        )

cond_template1=PromptTemplate(template="Write down a appropiate message for this positive feedback.\n {sentiment}",
                            input_variables=['sentiment'])
cond_template2=PromptTemplate(template="Write down a appropiate message for this negative feedback.\n {sentiment}",
                            input_variables=['sentiment'])


classifier_chain=template1|model1|parser_py

conditional_runnable=RunnableBranch(
    (lambda x:x.sentiment=='positive',cond_template1|model1|parser),
    (lambda x:x.sentiment=='negative',cond_template2|model1|parser),
    RunnableLambda(lambda x :"Didn't find anything")
)

chain=classifier_chain|conditional_runnable

output=chain.invoke({'feedback':'This is a horrible phone'})
print(output)

chain.get_graph().print_ascii()