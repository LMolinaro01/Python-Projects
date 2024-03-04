import os
import time


def adicionar(lista_filmes):

    os.system('cls')

    print("\n------------------------------")
    Nome = (input(f"\n|Insira o Nome do filme: "))
    Genero = (input("\n|Insira o Gênero/Temática do filme: "))
    Nota = float(input("\n|Insira a Nota do filme: "))
    Review = (input("\n|Insira sua Review/Comentários do filme: "))

    print("""\n(filme adicionado na lista com sucesso!)

------------------------------""")

    filme = {
        "Nome": Nome,
        "Genero": Genero,
        "Nota": Nota,
        "Review": Review,
    }

    lista_filmes.append(filme)

    time.sleep(2.1)


def exibir(lista_filmes):

    os.system('cls')

    if not lista_filmes:
        print("\nLista Vazia")
    else:
        print("----------------------------------------")
        for i, filme in enumerate(lista_filmes):
            print(f"""{i+1})
                  
 Nome: {filme ['Nome']},

 Genero: {filme ['Genero']},

 Nota: {filme ['Nota']},

 Review: {filme ['Review']}

----------------------------------------\n""")

    time.sleep(2)

    os.system('pause')


def editar(lista_filmes):

    exibir(lista_filmes)

    nome_filme = input("\n|Digite o nome do filme que deseja Editar: ")

    for filme in lista_filmes:
        if filme['Nome'] == nome_filme:

            os.system("cls")

            filme['Gênero'] = input(
                "\n|Insira o novo Gênero/Temática do filme: ")

            filme['Nota'] = float(input("\n|Insira a nova Nota do filme: "))

            filme['Review'] = input("\n|Insira a nova Review do filme: ")

            os.system('cls')

            print(f"""\n(filme editado com sucesso!)
                  
----------------------------------------
Resultado:
                      
 Nome: {filme ['Nome']},

 Genero (Editado): {filme ['Genero']},

 Nota (Editada): {filme ['Nota']},

 Review (Editada): {filme ['Review']}    

----------------------------------------""")

            time.sleep(1)

            os.system("pause")

            os.system('cls')

            return

    print("\n(Não há um filme com este nome na Lista, tente novamente.)\n")

    os.system("pause")

    os.system('cls')


def excluir(lista_filmes):

    os.system('cls')

    exibir(lista_filmes)

    nome_filme = input("\n|Digite o nome do filme que deseja Excluir: ")

    for filme in lista_filmes:
        if filme['Nome'] == nome_filme:
            lista_filmes.remove(filme)

            print("\n(O filme escolhido foi removido.)\n")

            os.system("pause")
            return

    print("\n(filme não encontrado na lista.)\n")

    os.system("pause")


def main():

    # Essa lista vai conter os filmes, 1 filme tem 4 categorias (dicionário)
    lista_filmes = []

    print("\n\n            ---| Bem vindo a sua Biblioteca de filmes! |---\n")

    time.sleep(3.5)

    while True:

        os.system('cls')

        escolha = int(input("""\n--> Faça sua escolha:\n      
|Adicionar (1)
        
|Editar (2)
        
|Excluir (3)
        
|Exibir (4)
        
|Sair (0)
        
Escolha: """))

        match escolha:

            case 1:
                adicionar(lista_filmes)
            case 2:
                editar(lista_filmes)
            case 3:
                excluir(lista_filmes)
            case 4:
                exibir(lista_filmes)
            case 0:
                os.system("cls")
                print("\n (Saindo...)\n")
                time.sleep(1.5)
                os.system("cls")

                return
            case _:
                print("\nOpção invalida, tente novamente")

if __name__ == "__main__":
    main()
