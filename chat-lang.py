from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()


chat = ChatOpenAI(model="gpt-4.1-nano-2025-04-14")
"""
# exemplo basico de chat
mensagens = [
    SystemMessage(content='vc é um assistente que conta piadas'),
    HumanMessage(content='o palmeiras tem mundial?')
]

resposta = chat.invoke(mensagens)
print(resposta.content)
"""

"""
# promp few-shot example
mensagens = [
    HumanMessage(content='quanto é 1+1?'),
    AIMessage(content='-> 2'),
    HumanMessage(content='quanto é 10+15'),
    AIMessage(content='-> 25'),
    HumanMessage(content='quanto é 1+15'),
]
resposta = chat.invoke(mensagens)
print(resposta.content)
"""