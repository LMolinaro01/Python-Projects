<h1 align = "center"> Projetos em Python </h1>

* [Simulador de Avaliações (Outro Repositório)](https://github.com/LMolinaro01/Simulador-de-Avaliacoes-em-Python/tree/main)
* [Sistema de Controle de Estoque](#Sistema-de-Estoque)

## Sistema de Estoque e Venda (Interface Visual, Banco de Dados, CRUD, Relógio em Tempo Real) <a name="Sistema-de-Estoque"></a>

Controle de estoque e venda desenvolvido em Python utilizando as bibliotecas Tkinter para a interface gráfica, SQLite para o armazenamento de dados, Datetime para registro das vendas (horário da venda), Time para um relógio funcional e Pillow (PIL) para a inserção de Imagens.

## Execução do Programa:
  
<p align="center">
  <a href="https://www.youtube.com/watch?v=ms-sq4UMDFw" target = "_blank">
    <img src="https://github.com/LMolinaro01/Projetos-e-Exercicios-em-Python/assets/126402616/a790994d-d796-422b-97f4-d078cfa32335">
  </a>
</p>

---

### Funcionalidades Principais:

- Adicionar produtos ao estoque.
- Editar informações de produtos existentes, incluindo a capacidade de modificar a quantidade em estoque ou remover produtos do registro.
- Visualizar o estoque atual.
- Alertas de estoque baixo.
- Interface gráfica intuitiva para os funcionários das lojas.
- Venda de Produtos
- Consulta de vendas (com o horário da venda)

### Tecnologias Utilizadas:

- Python
- Tkinter (para a interface gráfica)
- SQLite (para o armazenamento e gerenciamento dos dados do estoque)
- Pillow (PIL) (para manipulação de imagens)
- Time e Datetime (Registro de horário e Relógio funcional)

<h1 align = "center">Exercícios em Python</h1>

* [Biblioteca de Filmes](#biblioteca-de-filmes)
* [Criação de Classe e Instanciação de Objetos](#criação-de-classe-e-instanciação-de-objetos)
* [Calculadora utilizando Classe](#calculadora-utilizando-classe)
* [Calculadora de IMC](#calculadora-de-imc)
* [Regex no Python](#regex)
* [Interface Visual com TKinter](#tkinter1)
* [Utilizando um Banco de Dados local com SQLite3](#sqlite)


## Biblioteca de Filmes (Dicionário + CRUD) <a name="biblioteca-de-filmes"></a>


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

### Exemplo de Utilização - CRUD:

#### Adicionar Filme: 

``` py
---| Bem vindo a sua Biblioteca de filmes! |---

--> Faça sua escolha:
      
|Adicionar (1)
        
|Editar (2)
        
|Excluir (3)
        
|Exibir (4)
        
|Sair (0)
        
Escolha: 1

Insira o Nome do filme: Interestelar
Insira o Gênero/Temática do filme: Sci-Fi
Insira a Nota do filme: 9.5
Insira sua Review/Comentários do filme: Um filme incrível que explora as possibilidades do universo.

(Filme adicionado na lista com sucesso!)

------------------------------
```

#### Editar Filme:

``` py
--> Faça sua escolha:
      
|Adicionar (1)
        
|Editar (2)
        
|Excluir (3)
        
|Exibir (4)
        
|Sair (0)
        
Escolha: 2

----------------------------------------
1)
                  
 Nome: Interestelar,

 Genero: Sci-Fi,

 Nota: 9.5,

 Review: Um filme incrível que explora as possibilidades do universo.

----------------------------------------

Digite o nome do filme que deseja Editar: Interestelar
Insira o novo Gênero/Temática do filme: Sci-Fi, Drama
Insira a nova Nota do filme: 9.7
Insira a nova Review do filme: Uma jornada emocionante através do tempo e do espaço.

(Filme editado com sucesso!)

----------------------------------------
Resultado:
                      
 Nome: Interestelar,

 Genero (Editado): Sci-Fi, Drama,

 Nota (Editada): 9.7,

 Review (Editada): Uma jornada emocionante através do tempo e do espaço.

----------------------------------------
```

#### Excluir Filme:

``` py
--> Faça sua escolha:
      
|Adicionar (1)
        
|Editar (2)
        
|Excluir (3)
        
|Exibir (4)
        
|Sair (0)
        
Escolha: 3

----------------------------------------
1)
                  
 Nome: Interestelar,

 Genero: Sci-Fi, Drama,

 Nota: 9.7,

 Review: Uma jornada emocionante através do tempo e do espaço.

----------------------------------------

Digite o nome do filme que deseja Excluir: Interestelar

(O Filme escolhido foi Removido.)
```

#### Exibir Lista de Filmes:

``` py
--> Faça sua escolha:
      
|Adicionar (1)
        
|Editar (2)
        
|Excluir (3)
        
|Exibir (4)
        
|Sair (0)
        
Escolha: 4

(Lista Vazia...)
```

#### Sair do Programa:

``` py
--> Faça sua escolha:
      
|Adicionar (1)
        
|Editar (2)
        
|Excluir (3)
        
|Exibir (4)
        
|Sair (0)
        
Escolha: 0

(Saindo...)

```
---------------------------------------------------  

## Criação de Classe e Instanciação de Objetos <a name="criação-de-classe-e-instanciação-de-objetos"></a>


Este código é uma implementação em Python de uma classe "Guitarra", que permite criar objetos representando guitarras com diferentes características, como tamanho da corda, formato, afinação e captadores. A classe Guitarra possui métodos para tocar a guitarra e afiná-la.

* **Criando uma Classe:**
  
  ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/8f1601b9-f05a-4022-b7c4-17afb8459968)

Além da definição da classe Guitarra, o código também demonstra como criar objetos dessa classe e interagir com eles, solicitando informações do usuário para criar uma guitarra personalizada e exibindo informações sobre as guitarras criadas.

* **Instanciando Objetos:**
  
   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/69cb1532-ccf7-4a0d-8899-2c26d17748b1)

   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/21ee3c00-f7dc-4c31-a53c-71363da730ee)

* **Resultado:**

   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/1b56e332-e104-4102-9942-2e11d6a8d077)

  ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/4ed6c7bd-cea7-480b-94db-b07e62ed3368)

   ![image](https://github.com/LMolinaro01/Pequenos-Projetos-em-Python/assets/126402616/0e0c9df1-ae8a-46cc-b061-dae7040b422f)

---------------------------------------------------
## Calculadora utilizando Classe <a name="calculadora-utilizando-classe"></a>

### Funcionalidades do Programa:

| Operação       | Descrição                                                             |
|----------------|-----------------------------------------------------------------------|
| Adição         | Permite ao usuário somar dois números.                                |
| Subtração      | Permite ao usuário subtrair um número do outro.                       |
| Multiplicação  | Permite ao usuário multiplicar dois números.                           |
| Divisão        | Permite ao usuário dividir um número pelo outro. Se o segundo número for zero, exibe uma mensagem de erro. |
| Potência       | Permite ao usuário calcular a potência de um número, elevando-o a uma potência especificada. |
| Raiz Quadrada  | Permite ao usuário calcular a raiz quadrada de um número. Se o número for negativo, exibe uma mensagem de erro. |
| Sair           | Permite ao usuário encerrar o programa.                               |

### Exemplo de Utilização:

``` py
---------------- Calculadora ----------------

Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 4 #Usuário Escolheu Divisão

Digite o primeiro número: 10
Digite o segundo número: 0

Erro! Divisão por zero não é permitida.

Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 5 #Usuário escolheu Potência

Digite a base: 2
Digite o expoente: 3
Resultado: 8.0

Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 6 #Raiz Quadrada

Digite o número: 9
Resultado: 3.0

Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 7

Encerrando o programa...

```

1. **Adição:**
``` py
Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 1
Digite o primeiro número: 10
Digite o segundo número: 5

Resultado: 15.0
```

2. **Subtração:**
``` py
Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 2

Digite o primeiro número: 20
Digite o segundo número: 8

Resultado: 12.0
```

3. **Multiplicação:**
``` py
Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 3

Digite o primeiro número: 6
Digite o segundo número: 4

Resultado: 24.0
```

4. **Divisão:**
``` py
Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair
Digite a opção (1-7): 4

Digite o primeiro número: 50
Digite o segundo número: 5

Resultado: 10.0
```

5. **Potência:**
``` py
Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 5

Digite a base: 3
Digite o expoente: 4

Resultado: 81.0
```

6. **Raiz Quadrada:**
``` py
Selecione a operação:

1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz Quadrada
7. Sair

Digite a opção (1-7): 6

Digite o número: 64

Resultado: 8.0
```

Estes são exemplos de como cada operação funciona e o que é exibido para o usuário após a entrada dos números. O usuário pode continuar realizando operações ou sair do programa conforme necessário.

### Criação da Classe:

``` py
class Calculadora:
    def __init__(self):
        self.resultado = None

    def adicao(self, x, y):
        self.resultado = x + y
        return self.resultado

    def subtracao(self, x, y):
        self.resultado = x - y
        return self.resultado

    def multiplicacao(self, x, y):
        self.resultado = x * y
        return self.resultado

    def divisao(self, x, y):
        if y == 0:
            print("Erro! Divisão por zero não é permitida.")
            self.resultado = None
        else:
            self.resultado = x / y
        return self.resultado

    def potencia(self, x, y):
        self.resultado = x ** y
        return self.resultado

    def raiz_quadrada(self, x):
        if x < 0:
            print("Erro! Não é possível calcular a raiz quadrada de um número negativo.")
            self.resultado = None
        else:
            self.resultado = math.sqrt(x)
        return self.resultado
```
--------------------------------------------------
## Calculadora de IMC <a name="calculadora-de-imc"></a>

Este código Python apresenta duas versões de uma calculadora de Índice de Massa Corporal (IMC) que permite ao usuário inserir os nomes e pesos das pessoas, calculando seus respectivos IMCs e classificando-os de acordo com os padrões de classificação de IMC. Ambas as versões do código permitem a entrada de múltiplas pessoas, fornecendo uma descrição breve dos resultados ao final da entrada dos dados.

#### Recursos Utilizados:
* Utilização de listas para armazenar nomes, pesos e IMCs.
* Utilização de um loop While para permitir a entrada contínua de dados até que o usuário decida parar.
* Cálculo do IMC utilizando a fórmula: IMC = peso / (altura ^ 2).
* Utilização de estruturas condicionais If, Elif e Else para classificar os IMCs em categorias: Magro, Saudável, Sobrepeso e Obeso.
* Utilização de um loop For para percorrer os dados inseridos e determinar a pessoa com o maior e menor IMC.
* Utilização de variáveis para armazenar o maior e menor IMC, bem como os respectivos nomes das pessoas.

#### Exemplo de Utilização:

``` py
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
---------------------------------------------------
## Regex no Python <a name="regex"></a>

``` py

import re

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

# Exibir os endereços
enderecos = re.findall(r'Endereço: ([^\n]+)', dados)
print("Endereços:", enderecos)

# Exibir os salários
salarios = re.findall(r'Valor dos serviços: R\$ (\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))', dados)
print("Salários:", salarios)


```

#### Comandos para Procurar Algo:

* a -> Procura a Letra A
* . -> Procura qualquer coisa (menos pular linha)
* \d -> Procura um digito (\D procura o que não for um digito)
* \w -> alfanumérico (\W não alfanumérico)
* [abc] -> Procura A, B ou C
* \n -> Pular linha
  
#### Comandos para Determinar a Quantidade:

* "+" -> Pega o Máximo possível (1 a infinito)
* "*" -> Pega o Máximo (zero a infinito)
* {n} -> Pega N coisas
* | -> Comando OU

#### Comandos de Agrupamento:
* (?=...) -> Positive Lookahead
* (?<=...) -> Positive Lookbehind
* ( ) -> Agrupa

