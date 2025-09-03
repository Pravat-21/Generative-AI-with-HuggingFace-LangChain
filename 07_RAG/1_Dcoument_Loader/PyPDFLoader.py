from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(file_path="E:/CAMPUSX/GEN AI/CODE/7_RAG/1_Dcoument_Loader/Virtual evnv diff command.pdf")

docs=loader.load()
print(docs[0].page_content)