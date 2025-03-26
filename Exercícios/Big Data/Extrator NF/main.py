import re
import os

# Expressão regular para capturar apenas os valores após "Valor Total: R$"
regex = r"(?<=Valor Total:\sR\$)\s+([\d]{1,3}(?:\.\d{3})*(?:,\d{2})?)"

# Obtém a pasta onde o script está rodando
pasta_atual = os.path.dirname(os.path.abspath(__file__))

# Percorre todos os arquivos .txt na pasta
for arquivo in os.listdir(pasta_atual):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(pasta_atual, arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            valores_br = re.findall(regex, conteudo)  # Encontra todos os valores no formato BR

            # Converte para números float corretamente
            valores_numericos = [
                float(valor.replace('.', '').replace(',', '.')) for valor in valores_br
            ]

            # Pega apenas o terceiro valor, se existir
            valor_final = valores_numericos[2] if len(valores_numericos) >= 3 else "N/A"

            print(f"Arquivo: {arquivo}")
            print("Valor Total:", valor_final)
            print("-" * 50)
