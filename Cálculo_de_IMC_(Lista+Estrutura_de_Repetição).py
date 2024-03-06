nomes = []
pesos = []
imcs = []

nome = input(f"""\n--------------------------------
Digite o nome da pessoa: """)

while nome.lower() not in ("nao", "não"):
    peso = float(input("\nDigite o peso da pessoa (em kg): "))
    altura = float(input("\nDigite a altura da pessoa (em metros): "))
    
    nomes.append(nome)
    pesos.append(peso)
    
    imc = peso / (altura ** 2)
    imcs.append(imc)

    print(f"\nNome: {nome}, IMC: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Magro")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Saudável")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obeso")

    nome = input(f"""\n--------------------------------
Digite o nome da próxima pessoa ("Não" para Finalizar): """)

if nomes:

    indice_maior_imc = imcs.index(max(imcs))
     
    indice_menor_imc = imcs.index(min(imcs))

    print("\nPessoa com o maior IMC:")
    print(f"Nome: {nomes[indice_maior_imc]}, IMC: {imcs[indice_maior_imc]:.2f}")

    print("\nPessoa com o menor IMC:")
    print(f"Nome: {nomes[indice_menor_imc]}, IMC: {imcs[indice_menor_imc]:.2f}\n")
else:
    print("Nenhum dado foi inserido.")


#--------------------------------------------------------------------------------------------
#Outra versão do Código:

nomes = []
pesos = []
imcs = []

maior_peso = 0
menor_peso = 10000
nome_maior_peso = ""
nome_menor_peso = ""

continuar = True

while continuar:
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa (em kg): "))

    nomes.append(nome)
    pesos.append(peso)

    resposta = input("Deseja adicionar outra pessoa? (Sim/Não): ")

    if resposta.lower() not in "sim":
        continuar = False

for i in range(len(nomes)):
    peso = pesos[i]
    altura = float(input(f"Digite a altura de {nomes[i]} (em metros): "))
    imc = peso / (altura ** 2)
    imcs.append(imc)

    print(f"Nome: {nomes[i]}, IMC: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Magro")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Saudável")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obeso")

    if imc < menor_peso:
        menor_peso = imc
        nome_menor_peso = nomes[i]
    if imc > maior_peso:
        maior_peso = imc
        nome_maior_peso = nomes[i]

print("\nPessoa com o maior IMC:")
print(f"Nome: {nome_maior_peso}, IMC: {maior_peso:.2f}")

print("\nPessoa com o menor IMC:")
print(f"Nome: {nome_menor_peso}, IMC: {menor_peso:.2f}")
