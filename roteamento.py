from langchain_openai.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnablePassthrough

import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini-2024-07-18')

prompt = ChatPromptTemplate.from_template(''' Você é um professor de matemática do ensino médio capaz de dar respostas
muito detalhadas e deidáticas. Responda a seguinte pergunta de um aluno: 
Pergunta: {pergunta}''')
chain_matematica =  prompt | model | StrOutputParser()

prompt = ChatPromptTemplate.from_template(''' Você é um professor de física do ensino médio capaz de dar respostas
muito detalhadas e deidáticas. Responda a seguinte pergunta de um aluno: 
Pergunta: {pergunta}''')
chain_fisica =  prompt | model | StrOutputParser()

prompt = ChatPromptTemplate.from_template(''' Você é um professor de história do ensino médio capaz de dar respostas
muito detalhadas e deidáticas. Responda a seguinte pergunta de um aluno: 
Pergunta: {pergunta}''')
chain_historia =  prompt | model | StrOutputParser()


prompt = ChatPromptTemplate.from_template(''' {pergunta} ''')
chain_generica = prompt | model | StrOutputParser()


############ roteamento ################


########## padronizar a chain p receber pergunta
prompt = ChatPromptTemplate.from_template('Voce deve categorizar a seguinte pergunta: {pergunta}')

class Categorizador(BaseModel):
    """Categoriza as perguntas de alunos do ensino médio """
    area_conhecimento: str= Field(description='A area de comnhecimento da pergunta feita pelo aluno. \
    Deve ser "física", "matemática" ou "hitória". Caso não se encaixe em nenhuma delas, retorne "outra"')
    
model_estruturado = prompt | model.with_structured_output(Categorizador)

resposta = model_estruturado.invoke({'pergunta':'quem descobriu a américa?'})

print(resposta)


##############################

chain = RunnablePassthrough().assign(categoria = model_estruturado)
chain.invoke({'pergunta':'quem descobriu a américa?'})

def route(input):
    if input['categoria'].area_conhecimento == 'matemática':
        return chain_matematica
    if input['categoria'].area_conhecimento == 'física':
        return chain_fisica
    if input['categoria'].area_conhecimento == 'história':
        return chain_historia
    return chain_generica

chain = RunnablePassthrough().assign(categoria = model_estruturado) | route | StrOutputParser()
resposta_route = chain.invoke({'pergunta':'oq é a fórmula h2o?'})

print(resposta_route)