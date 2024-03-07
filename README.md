# Exercícios em Python

* Cálculo de IMC (Utilizando Listas e Coleta de Dados do Usuário)
* Biblioteca de Filmes
* Criação de Classe e Instanciação de Objetos


## Biblioteca de Filmes (Dicionário + CRUD)


Este é um programa em Python para gerenciar uma biblioteca de filmes. Ele oferece funcionalidades para adicionar, editar, excluir e exibir filmes na lista, permitindo ao usuário organizar sua coleção de filmes de forma simples e eficiente.

### Funcionalidades

*   **Adicionar Filme:** Permite ao usuário adicionar um novo filme à lista, inserindo o nome do filme, gênero, nota e uma revisão ou comentários sobre o filme.
   
    ![image](https://github.com/LMolinaro01/Biblioteca-de-Filmes-em-Python/assets/126402616/c84241bc-7042-46bf-8ff9-259174cf6377)
    
*   **Exibir Filmes:** Exibe todos os filmes presentes na lista, mostrando o nome do filme, gênero, nota e revisão.
  
    ![image](https://github.com/LMolinaro01/Biblioteca-de-Filmes-em-Python/assets/126402616/af96ca04-db2a-429e-bbf5-97bce510a75e)
    
*   **Editar Filme:** Permite ao usuário editar as informações de um filme existente na lista, incluindo o gênero, nota e revisão.
  
    ![image](https://github.com/LMolinaro01/Biblioteca-de-Filmes-em-Python/assets/126402616/392d5c1b-a651-4cef-bbda-118ca370dc7a)
    
*   **Excluir Filme:** Permite ao usuário excluir um filme da lista, inserindo o nome do filme que deseja remover.
  
    ![image](https://github.com/LMolinaro01/Biblioteca-de-Filmes-em-Python/assets/126402616/3c54b037-cebd-450c-830a-cd423e954deb)
    
    ![image](https://github.com/LMolinaro01/Biblioteca-de-Filmes-em-Python/assets/126402616/1701f0ff-0220-4ea4-88fb-9b64efe95fb2)
    
*   **Sair:** Encerra o programa

---------------------------------------------------  

## Criação de Classe e Instanciação de Objetos


Este código é uma implementação em Python de uma classe `Guitarra`, que permite criar objetos representando guitarras com diferentes características, como tamanho da corda, formato, afinação e captadores. A classe `Guitarra` possui métodos para tocar a guitarra e afiná-la.

* **Criando uma Classe:**
  
  ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/8f1601b9-f05a-4022-b7c4-17afb8459968)

Além da definição da classe `Guitarra`, o código também demonstra como criar objetos dessa classe e interagir com eles, solicitando informações do usuário para criar uma guitarra personalizada e exibindo informações sobre as guitarras criadas.

* **Instanciando Objetos:**
  
   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/69cb1532-ccf7-4a0d-8899-2c26d17748b1)

   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/21ee3c00-f7dc-4c31-a53c-71363da730ee)

* **Resultado:**

   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/1b56e332-e104-4102-9942-2e11d6a8d077)

  ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/4ed6c7bd-cea7-480b-94db-b07e62ed3368)

   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/0e0c9df1-ae8a-46cc-b061-dae7040b422f)

---------------------------------------------------

## Descrição do Código - Calculadora de IMC

Este código Python apresenta duas versões de uma calculadora de Índice de Massa Corporal (IMC) que permite ao usuário inserir os nomes e pesos das pessoas, calculando seus respectivos IMCs e classificando-os de acordo com os padrões de classificação de IMC. Ambas as versões do código permitem a entrada de múltiplas pessoas, fornecendo uma descrição breve dos resultados ao final da entrada dos dados.

#### Recursos Utilizados:
* Utilização de listas para armazenar nomes, pesos e IMCs.
* Utilização de um loop `while` para permitir a entrada contínua de dados até que o usuário decida parar.
* Cálculo do IMC utilizando a fórmula: IMC = peso / (altura ^ 2).
* Utilização de estruturas condicionais `if`, `elif` e `else` para classificar os IMCs em categorias: Magro, Saudável, Sobrepeso e Obeso.
* Utilização de um loop `for` para percorrer os dados inseridos e determinar a pessoa com o maior e menor IMC.
* Utilização de variáveis para armazenar o maior e menor IMC, bem como os respectivos nomes das pessoas.

#### Exemplo de Utilização:

```
Digite o nome da pessoa: João
Digite o peso da pessoa (em kg): 70
Digite a altura da pessoa (em metros): 1.75

Nome: João, IMC: 22.86
Classificação: Saudável

Deseja adicionar outra pessoa? (Sim/Não): sim
Digite o nome da pessoa: Maria
Digite o peso da pessoa (em kg): 55
Digite a altura da pessoa (em metros): 1.60

Nome: Maria, IMC: 21.48
Classificação: Saudável

Deseja adicionar outra pessoa? (Sim/Não): não

Pessoa com o maior IMC:
Nome: João, IMC: 22.86

Pessoa com o menor IMC:
Nome: Maria, IMC: 21.48
```
