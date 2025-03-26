import re
import os


#(?=Valor Total:\s*R\$\s*([\d,]*))
#Não pega 200.000,00

#(?<=Valor Total:\sR\$)\s+([\d]{1,3}(?:[.\d]{3})*(?:,\d{2})?)
#Pega 200.000,00

regex = r"(?<=Valor Total:\sR\$)\s+([\d]{1,3}(?:[.\d]{3})*(?:,\d{2})?)"

pasta_atual = os.path.dirname(os.path.abspath(__file__))


for arquivo in os.listdir(pasta_atual):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(pasta_atual, arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            valores = re.findall(regex, conteudo)
            print(f"Arquivo: {arquivo}")
            print("Valores encontrados:", valores)
            print("-" * 50)