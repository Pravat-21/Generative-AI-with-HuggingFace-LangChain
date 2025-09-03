from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1", 
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact 1',description='fact 1 about the topic'),
    ResponseSchema(name='fact 2',description='fact 2 about the topic'),
    ResponseSchema(name='fact 3',description='fact 3 about the topic')
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(template="Give me 3 facts about {topic}\n {format_instruction}",
                        input_variables=['topic'],
                        partial_variables={'format_instruction':parser.get_format_instructions()}
                        )
chain= template|model|parser
output=chain.invoke({'topic':'wake up in early morning'})
print(output)