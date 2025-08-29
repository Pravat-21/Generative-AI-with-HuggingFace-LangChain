from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model1=ChatHuggingFace(llm=llm)
model2=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(template="Generate a beautiful notes of the following text \n {text}",
                       input_variables=['text']
                       )
prompt2=PromptTemplate(template="Generate 5 most important quiz from this  following text \n {text}",
                       input_variables=['text']
                       )
prompt3=PromptTemplate(template="Marge this following text & quiz and make a single document \n text-{my_note} & quiz={quiz}",input_variables=['my_note','quiz']
                       )

parser=StrOutputParser()

## we have to keep the name of chain according to the name of input variables which are going to be used in next prompt.
parallel_chain=RunnableParallel({
    'my_note': prompt1|model1|parser,  
    'quiz': prompt2|model2|parser
})

marger_chain=prompt3|model1|parser

chain = parallel_chain|marger_chain

text="""Agentic AI is a class of artificial intelligence that focuses on autonomous systems that can make decisions and perform tasks without human intervention. The independent systems automatically respond to conditions, to produce process results. The field is closely linked to agentic automation, also known as agent-based process management systems, when applied to process automation. Applications include software development, customer support, cybersecurity and business intelligence.The core concept of agentic AI is the use of AI agents to perform automated tasks without human intervention.While robotic process automation (RPA) systems automate rule-based, repetitive tasks with fixed logic, agentic AI adapts and learns from data inputs. Agentic AI refers to autonomous systems capable of pursuing complex goals with minimal human intervention, often making decisions based on continuous learning and external data. Functioning agents can require various AI techniques, such as natural language processing, machine learning (ML), and computer vision, depending on the environment.

Particularly, reinforcement learning (RL) is essential in assisting agentic AI in making self-directed choices by supporting agents in learning best actions through the trial-and-error method. Agents using RL continuously to explore their surroundings will be given rewards or punishment for their actions, which refines their decision-making capability over time. All the while deep learning, as opposed to rule-based methods, supports agentic AI through multi-layered neural networks to learn features from extensive and complex sets of data. Further, multimodal learning enable AI agents to integrate various types of information, such as text, images, audio and video.[4] As a result, agentic AI systems are capable of making independent decisions, interacting with their environment and optimising processes without a human directly intervening.
"""

result=chain.invoke({'text':text})
print(result)

# in order to see the graph

chain.get_graph().print_ascii()


