import requests
import json
from datetime import datetime
import os

# URL da API gratuita
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # Lança erro se a requisição falhar

    # Extrai o valor da cotação do JSON retornado
    dados_api = resposta.json()
    cotacao_texto = dados_api["USDBRL"]["bid"]
    cotacao_valor = float(cotacao_texto)

    # Data e hora atual
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nova_cotacao = {
        "data_hora": agora,
        "cotacao_dolar": cotacao_valor
    }

    # Nome do arquivo onde vamos salvar os dados
    nome_arquivo = "cotacoes.json"

    # Verifica se o arquivo já existe
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = []

    # Adiciona a nova cotação à lista
    dados.append(nova_cotacao)

    # Salva no arquivo JSON
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Cotação capturada: R$ {cotacao_valor}")
    print("Cotação salva com sucesso em cotacoes.json")

except Exception as e:
    print("Erro ao obter a cotação:", e)
