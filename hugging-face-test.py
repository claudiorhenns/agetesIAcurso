from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()
hf_token   = os.getenv("HUGGINGFACEHUB_API_TOKEN")

modelo = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

llm = HuggingFaceEndpoint(repo_id=modelo, huggingfacehub_api_token=hf_token)
chat = ChatHuggingFace(llm=llm)
response = chat.invoke("Olá, como vai?")
print(response)