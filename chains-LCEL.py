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

respostaChain1 = chain.invoke({'tema': 'santos dos ultimos dias'})

print(respostaChain1)

#################chain que traduz texto para ingles ##################

promptTradutor = ChatPromptTemplate.from_template('traduza o texto {texto} para o inglês')

chainTradutor = promptTradutor | model | StrOutputParser()

respostaTradutor = chainTradutor.invoke({'texto': 'eu amo criar jogos de video game'})

print(respostaTradutor)

#################chain que resume um texto ##################

promptResume = ChatPromptTemplate.from_template('resuma o texto {texto} em 5 palavras em ingles')

chainResume = promptResume | model | StrOutputParser()

respostaResumo = chainResume.invoke({'texto': 'Os santos dos últimos dias são exemplos de fé e perseverança, mostrando que é possível viver uma vida digna em meio às adversidades.'})

print(respostaResumo)

#################chain que junta as outras 2 chains ##################

textoFull = 'Os santos dos últimos dias são exemplos de fé e perseverança, mostrando que é possível viver uma vida digna em meio às adversidades.'

chainFull = chainTradutor | chainResume

respostaFull = chainFull.invoke({'texto': textoFull})

print(respostaFull)

