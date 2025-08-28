from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

template=ChatPromptTemplate([
    ('system','You are very good Ai assistant.'),
    MessagesPlaceholder(variable_name='chat_history_refund'),
    ('human','{query}')
])

chat_history=[]
with open("Prompts/refund_history.txt") as f:
    chat_history.extend(f.readlines())


prompt=template.invoke({
    'chat_history_refund':chat_history,
    'query': 'where is my refund'
})


print(prompt)
