from langchain_openai.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()


chat = ChatOpenAI()
outputparser = StrOutputParser()

chat_template = ChatPromptTemplate.from_messages(
    [
    ('system', 'Você é um assitente engraçado e se chama {nome_assistente}'),
    ('human', '{pergunta}')
    ]
 )


#chat_template.format_messages(nome_assistente='Rhenns', pergunta='qual seu nome?')

prompt = chat_template.invoke({'nome_assistente':'Rhenns', 'pergunta':'qual seu nome?'})

resposta = chat.invoke(prompt)

# faz a mesma coisa que resposta.content
print(outputparser.invoke(resposta))

### spolier de CHAINS ###
chain = chat_template | chat | outputparser

resultado_chain= chain.invoke({'nome_assistente':'Rhenns', 'pergunta':'qual seu nome?'})
print(resultado_chain)
#########################



### output structured ###

from typing import Optional
from pydantic import BaseModel, Field

class Piada(BaseModel):
    """Piada para contar ao usuário """
    introducao: str= Field(description='A introdução da piada')
    punchline: str= Field(description='A conclusao da piada')
    avaliacao: Optional[int]= Field(description='O quaão boa é a piada de 0 a 10')

lll_estruturada = chat.with_structured_output(Piada)
resposta_piada = lll_estruturada.invoke('conte uma piada sobre o palmeiras')

print(resposta_piada)
print(resposta_piada.introducao)
print(resposta_piada.punchline)
print(resposta_piada.avaliacao)
#############################

########## exemplo de avaliação de review ############
review_cliente ="""Esse mix de frunta sé muitolegal. Ele tem 3 velocidades. Chegou em 3 dias, sendo 2 dias antes do prazo determinado
                    Estou muito satisfeito com a compra. Um unico problema que tenho a relatar, um ponto negativo, é
                    que ele faz muito barulho."""

class AvaliacaoReview(BaseModel):
    """Avalia review do cliente """
    presente: bool= Field(description='Verdadeiro se foi para presente e falso se não foi')
    dias_entrega: str= Field(description='Quantos dias para entrega do produto')
    percepcao_valor: list[str]= Field(description='extraia qualquer frase sobre o valor ou preço do produto. Retorne uma lista')

lll_estruturada = chat.with_structured_output(AvaliacaoReview)
resposta_review = lll_estruturada.invoke(review_cliente)

print(resposta_review)
print(resposta_review.presente)
print(resposta_review.dias_entrega)
print(resposta_review.percepcao_valor)