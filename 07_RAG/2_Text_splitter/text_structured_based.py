from langchain.text_splitter import RecursiveCharacterTextSplitter

text="""
My name is Pravat.
I am 26 years old. 

I live in Kolkata. 
How are you.
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
)

output=splitter.split_text(text)
print(output)
print(len(output))