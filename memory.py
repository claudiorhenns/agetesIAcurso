from langchain_openai.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnablePassthrough
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini-2024-07-18')

memory = InMemoryChatMessageHistory()

memory.add_user_message('ola modelo')
memory.add_ai_message('olá user')

print(memory.messages)

################   exemplo   ####################################
prompt = ChatPromptTemplate.from_messages([
    ('system', 'Você é um tutor de programação chamado Rhenns. responda as perguntas de forma didática'),
    ('placeholder','{history}'),
    ('human','{pergunta}'),
])

chain = prompt | model | StrOutputParser()

store = {}

def get_by_session_id(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain_com_memoria = RunnableWithMessageHistory(chain, get_by_session_id, input_messages_key='pergunta',history_messages_key='history')
config = {'configurable': {'session_id':'usuario_a'}}

resposta = chain_com_memoria.invoke({'pergunta': 'olá, meu nome é claudio?'}, config=config)

print(resposta)

resposta = chain_com_memoria.invoke({'pergunta': 'qual o meu nome?'}, config=config)

print(resposta)