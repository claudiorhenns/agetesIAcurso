from langchain_openai.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()

model = ChatOpenAI()

prompt = ChatPromptTemplate.from_template('Crie uma frase sobre o tema: {tema}')

chain = prompt | model | StrOutputParser()
################### roda varias chains simutaneas ##################
respostaChain1 = chain.batch([{'tema': 'santos dos ultimos dias'}, {'tema': 'video games'}, {'tema': 'IA'}])

print(respostaChain1)