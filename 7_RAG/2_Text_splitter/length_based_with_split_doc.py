from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(file_path="E:/CAMPUSX/GEN AI/CODE/7_RAG/1_Dcoument_Loader/Virtual evnv diff command.pdf")

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_documents(docs)
print(result[2].page_content)
print(len(result))