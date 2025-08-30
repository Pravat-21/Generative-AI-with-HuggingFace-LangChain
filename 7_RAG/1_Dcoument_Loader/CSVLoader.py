from langchain_community.document_loaders import CSVLoader

loader=CSVLoader("E:/CAMPUSX/GEN AI/CODE/7_RAG/1_Dcoument_Loader/Social_Network_Ads.csv")
docs=loader.load()

print(docs[0].page_content)
print(len(docs))
