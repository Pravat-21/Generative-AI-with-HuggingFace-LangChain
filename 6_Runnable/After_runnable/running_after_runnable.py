from components_rnble import FakeLLM,FakePromptTemplate,FakestrOutputParser,ChainConnector

model=FakeLLM()

template=FakePromptTemplate(template="Write something about {topic}",input_variables=['topic'])

parser=FakestrOutputParser()

chain=ChainConnector([template,model,parser])
output=chain.invoke({'topic':'football'})

print(output)