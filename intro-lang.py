from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()


llm = OpenAI()
"""
question = "me conte um historia de 200 palavras sobre a capital do Brasil"

for trecho in llm.stream(question):
    print(trecho, end="")
"""

############
#respostas = llm.invoke(question)
#print(respostas)

perguntas =[
    'qual a maior torcida do Brasil?',
    'quem foi pelé?',
    'quem é o atual campeao brasileiro de futebol?'
]

respostas = llm.batch(perguntas)
print(respostas)