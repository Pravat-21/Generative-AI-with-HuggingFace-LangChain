from components import FakeLLM,FakePromptTemplate,FakestrOutputParser

my_model=FakeLLM()

template=FakePromptTemplate(template="Tell me something about {topic}",input_variables=['topic'])
prompt=template.format_template({'topic':'football'})
print("This is template output-->",prompt)

output=my_model.predict(prompt)
print("This is model output-->",output)

parser=FakestrOutputParser()

print("This is parser output-->",parser.parse(output))