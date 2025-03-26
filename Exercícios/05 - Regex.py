#Regex:

#Procurar alguma coisa
#Definir a qtde de alguma coisa
#Agrupar alguma coisa


import re

#3 regex: 1 para data, um para valor e endereço

# String contendo os dados das duas pessoas
dados = """
Nome: pedro dos santos             Data nascimento: 01/01/2000
cpf: 123.456.789-00       Endereço: rua exemplo
                                loja 3
Valor dos serviços: R$ 1.200,00
Tipo de contrato: Mei
--------------------------------------------------------------
Nome: ana             Data nascimento: 01-01-2010
cpf: 123.456.789-00       Endereço: exemplo rua
Valor dos serviços: R$ 1200
Tipo de contrato: clt
"""

# Exibir todos os nomes
nomes = re.findall(r'Nome: ([^\n]+)', dados)
# Remover as informações depois do nome (data de nascimento)
nomes = [nome.split()[0] for nome in nomes]
print("Nomes:", nomes)

# Exibir as datas de nascimento
datas_nascimento = re.findall(r'Data nascimento: (\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})', dados)
print("Datas de Nascimento:", datas_nascimento)

#alternativa mais abrangente ((?<=Data nascimento:|data nascimento:|data de nascimento:|Data de Nascimento:|Data nascimento|data nascimento|data de nascimento|Data de Nascimento:) \d{2}\/\d{2}\/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}\/\d{2}\/\d{2}|\d{2}-\d{2}-\d{2})

# Exibir os endereços
enderecos = re.findall(r'Endereço: ([^\n]+)', dados)
print("Endereços:", enderecos)

# Exibir os salários
salarios = re.findall(r'Valor dos serviços: R\$ (\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))', dados)
print("Salários:", salarios)
