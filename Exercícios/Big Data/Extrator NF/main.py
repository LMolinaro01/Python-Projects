import re
import os
import pandas as pd

# Expressão regular para capturar apenas os valores após "Valor Total: R$"
regex = r"(?<=Valor Total:\sR\$)\s+([\d]{1,3}(?:\.\d{3})*(?:,\d{2})?)"

# Obtém a pasta onde o script está rodando
pasta_atual = os.path.dirname(os.path.abspath(__file__))

# Listas para armazenar dados
arquivos = []
valores = []

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

            # Armazena os dados para a tabela
            arquivos.append(arquivo)
            valores.append(valor_final)

# Cria um DataFrame com os dados
df = pd.DataFrame({
    'Arquivo': arquivos,
    'Valor Total': valores
})

# Converte para números float, ignorando "N/A"
df['Valor Total'] = pd.to_numeric(df['Valor Total'], errors='coerce')

# Formata os valores como R$ XXX.XXX,XX
df['Valor Total'] = df['Valor Total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Calcula a soma total
soma_total = df['Valor Total'].apply(lambda x: float(x.replace("R$ ", "").replace(".", "").replace(",", "."))).sum()

# Cria uma nova linha com a soma total
soma_df = pd.DataFrame({
    'Arquivo': ['Total'],
    'Valor Total': [f"R$ {soma_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")]
})

# Adiciona a nova linha de total ao DataFrame
df = pd.concat([df, soma_df], ignore_index=True)

# Exibe a tabela
print(df)

# Salva a tabela em um arquivo CSV (opcional)
#df.to_csv('nota_fiscal_valores.csv', index=False)
