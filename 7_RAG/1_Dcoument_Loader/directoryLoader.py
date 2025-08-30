from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="E:/CAMPUSX/GEN AI/CODE/7_RAG/1_Dcoument_Loader/mypdf",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

doc=loader.load()
print(doc[0].page_content)
print(len(doc)) # total no. of pages is 344

