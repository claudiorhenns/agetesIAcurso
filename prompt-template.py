from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv

# carrega variáveis do .env para o os.environ
load_dotenv()


llm = OpenAI()

prompt_template = PromptTemplate.from_template('''
responda a seguinte pergunta do usuario em {n_palavras} palavras:
{pergunta}
''', partial_variables={'n_palavras':10})

prompt_lingua = PromptTemplate.from_template('''
responda em {lingua}
''', partial_variables={'lingua':'portugues'})

prompt_final = (prompt_template + prompt_lingua)


#response = prompt_template.format(pergunta='oq é o sol?', n_palavras=50)

prompt = prompt_final.format(pergunta='oq é o sol?', n_palavras=50, lingua='ingles')

response = llm.invoke(prompt)
print(response)