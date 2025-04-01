import re

"""
Este script utiliza expressões regulares (Regex) para extrair informações específicas de um conjunto de dados.

1. **Procurar alguma coisa**: Utilizamos padrões regex para localizar nomes, datas de nascimento, endereços e valores monetários.
2. **Definir a quantidade de alguma coisa**: Empregamos quantificadores para definir a quantidade exata de caracteres que estamos buscando (ex: `\d{2}/\d{2}/\d{4}`).
3. **Agrupar alguma coisa**: Usamos parênteses `()` para capturar grupos específicos dentro das expressões.
"""

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
nomes = re.findall(r'(?<=Nome: )\s*([^\d\n]+?)\s*(?=Data nascimento|Data de nascimento|$)', dados)
print("Nomes:", nomes)

# Exibir as datas de nascimento
datas_nascimento = re.findall(r'(?<=Data nascimento:|data nascimento:|data de nascimento:|Data de Nascimento:)\s*(\d{2}[/-]\d{2}[/-]\d{4}|\d{2}[/-]\d{2}[/-]\d{2})', dados)
print("Datas de Nascimento:", datas_nascimento)

# Exibir os endereços
enderecos = re.findall(r'(?<=Endereço: )(.+\s)+?(?=Valor dos serviços)', dados)
print("Endereços:", enderecos)

# Exibir os salários
salarios = re.findall(r'(?<=Valor dos Serviços: R\$ )(\d.,)+', dados)
print("Salários:", salarios)
