from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

pergunta = input("O Que deseja saber?: ")
resposta = llm.invoke(str(pergunta))

print(resposta.content)