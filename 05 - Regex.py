import re

# String contendo os dados das duas pessoas
dados = """
Nome: pedro dos santos             Data nascimento: 01/01/2000
cpf: 123.456.789-00       Endereço: nova america, del castilho
                                loja 3
Valor dos serviços: R$ 1.200,00
Tipo de contrato: Mei
--------------------------------------------------------------
Nome: ana             Data nascimento: 01-01-2010
cpf: 123.456.789-00       Endereço: norte shop
Valor dos serviços: R$ 1200
Tipo de contrato: clt
"""

#Exibi todos os nomes
nomes = re.findall(r'Nome: ([^\n]+)', dados)
# Removi as informações dps do nome (data de nascimento)
nomes = [nome.split()[0] for nome in nomes]
print("Nomes:", nomes)

#Exibi as datas de nascimento
datas_nascimento = re.findall(r'Data nascimento: (\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})', dados)
print("Datas de Nascimento:", datas_nascimento)

#Exibi os salários
salarios = re.findall(r'Valor dos serviços: R\$ (\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))', dados)
print("Salários:", salarios)
