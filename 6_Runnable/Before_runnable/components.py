import random

class FakeLLM:
    def __init__(self):
        pass

    def predict(self,prompt):
        response=['Delhi is the capital of India','Ronaldo is better than messi in term of physical ability','Heheheheheheheheeheheehe']
        if 'cricket' in prompt:
            return {'response':"Cricket is a bat-and-ball sport played between two teams of 11 players, popular worldwide, especially in countries like India, England, and Australia.It combines strategy, skill, and endurance, with formats ranging from fast-paced T20s to five-day Test matches."}
        elif 'football' in prompt:
            return {'response':"Football (soccer) is the world’s most popular sport, played between two teams of 11 players aiming to score goals by getting the ball into the opponent’s net.It’s celebrated globally for its simplicity, passion, and major events like the FIFA World Cup."}
        else:
            return {'response':random.choice(response)}


class FakePromptTemplate:

    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables

    def format_template(self,input_dict):
        return self.template.format(**input_dict)
    

class FakestrOutputParser:

    #def __init__(self):
        #pass

    def parse(self,dict):
        return dict['response']


