import re

# String contendo os dados das duas pessoas
dados = """
Nome: João
Data de Nascimento: 01/01/1990
Salário: R$ 3,500.00

Nome: Maria
Data de Nascimento: 1995-05-05
Salário: R$ 4.200,00
"""

# Comando 1: Exibir todos os nomes
nomes = re.findall(r'Nome: (\w+)', dados)
print("Nomes:", nomes)

# Comando 2: Exibir as datas de nascimento
datas_nascimento = re.findall(r'Data de Nascimento: (\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})', dados)
print("Datas de Nascimento:", datas_nascimento)

# Comando 3: Exibir os salários
salarios = re.findall(r'Salário: R\$ (\d+(?:[.,]\d{2}))', dados)
print("Salários:", salarios)
