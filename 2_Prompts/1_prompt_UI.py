from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

my_model=ChatHuggingFace(llm=llm)

st.header("Research Paper Summarization Tools")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template=load_prompt('template.json')



if st.button("Answer"):
    chain= template | my_model
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })
    st.write(result.content)