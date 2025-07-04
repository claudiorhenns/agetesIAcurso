from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
import os
from dotenv import load_dotenv

from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.cache import SQLiteCache

# carrega variáveis do .env para o os.environ
load_dotenv()


chat = ChatOpenAI(model="gpt-4.1-nano-2025-04-14")
## opçao de cache normal
set_llm_cache(InMemoryCache())

## opção de salvar o arquivo
set_llm_cache(SQLiteCache(database_path='C:/Users/famil/Documents/PROJETOS - IA - CHATBOT-WHATSAPP/curso-agentes-IA/data.sqlite'))

mensagens = [
    SystemMessage(content='vc é um assistente engraçado'),
    HumanMessage(content='quanto é 1+1?')
]

resposta = chat.invoke(mensagens)
print(resposta.content)