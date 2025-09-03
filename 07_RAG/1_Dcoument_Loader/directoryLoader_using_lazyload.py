from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="E:/CAMPUSX/GEN AI/CODE/7_RAG/1_Dcoument_Loader/mypdf",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

"""doc=loader.load()
for document in doc:
    print(document.metadata)"""

doc=loader.lazy_load()
for document in doc:
    print(document.metadata) # it has taken less time than previous.