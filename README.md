<h1 align = "center"> Projetos em Python </h1>

* [Snap Link (Security Cam)](https://github.com/LMolinaro01/SnapLink)
* [Gerador de Polígonos](https://github.com/LMolinaro01/Gerador-de-Poligonos) 
* [Sistema de Venda e Controle de Estoque](#Sistema-de-Estoque)
* [Sistema de Controle de Estoque (PostgreSQL)](#Sistema-de-EstoquePSQL)
* [Youtube Downloader](https://github.com/LMolinaro01/Youtube-Downloader) 
* [Simulador de Avaliações](https://github.com/LMolinaro01/Simulador-de-Avaliacoes-em-Python/tree/main)


<h1 align = "center">Exercícios em Python</h1>

### Exercícios Introdutórios (POO/CRUD/GUI/SQLite)

* [Biblioteca de Filmes](#biblioteca-de-filmes)
* [Criação de Classe e Instanciação de Objetos](#criação-de-classe-e-instanciação-de-objetos)
* [Calculadora utilizando Classe](#calculadora-utilizando-classe)
* [Calculadora de IMC](#calculadora-de-imc)
* [Interface Visual com TKinter](#tkinter1)
* [Utilizando um Banco de Dados local com SQLite3](#sqlite)

### Manipulação de String

* [Regex no Python](#regex)
* [Guia Completo de Regex](#guiaregex)

### Big Data

* [Extrator de Nota Fiscal com Regex e Pandas](#nfpanda)
* [Fatos de Gatos + Tradução (API) com Regex e CustomTkinter](#gatofato)

### Manipulação de Arquivos

* [UnifyFiles - Organizador de Arquivos em Pasta Principal](#)
* [PDF Merger - Unificador de Arquivos PDF](#)
* [MKV Subtitle Picker - Extrator de Legendas de Arquivos MKV](#)

# Sistema de Venda e Controle de Estoque <a name="Sistema-de-Estoque"></a>

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

---

# Sistema de Venda e Controle de Estoque <a name="Sistema-de-EstoquePSQL"></a>

Este projeto é um sistema de gerenciamento de estoque desenvolvido em Python, utilizando o banco de dados PostgreSQL para armazenar as informações dos produtos. O sistema permite realizar operações básicas de CRUD (Create, Read, Update, Delete) em um ambiente de linha de comando.

![image](https://github.com/user-attachments/assets/d6b10ac0-734b-438f-af66-dee24327fc4f) (imagem meramente ilustrativa)


## Funcionalidades

- **Adicionar Produto**: Permite inserir um novo produto no estoque, solicitando informações como nome, quantidade e preço.
- **Visualizar Produtos**: Exibe uma lista de todos os produtos cadastrados no sistema, incluindo seus detalhes.
- **Atualizar Produto**: Possibilita a atualização das informações de um produto existente, como alteração de quantidade ou preço.
- **Deletar Produto**: Permite remover um produto do estoque com base em seu identificador único.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada para desenvolver a lógica do sistema.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar as informações dos produtos.
- **psycopg2**: Biblioteca Python que facilita a conexão e interação com o banco de dados PostgreSQL.

## Estrutura do Código

O código é estruturado em funções que correspondem às operações de CRUD mencionadas. Cada função estabelece uma conexão com o banco de dados, executa a operação desejada e, em seguida, fecha a conexão. O fluxo principal do programa apresenta um menu interativo que permite ao usuário selecionar a operação que deseja realizar.

## Configuração e Execução

1. **Instalação das Dependências**: Certifique-se de que o Python e o PostgreSQL estão instalados em seu sistema. Instale a biblioteca `psycopg2` utilizando o pip:

   ```bash
   pip install psycopg2
   ```


2. **Configuração do Banco de Dados**: Crie um banco de dados no PostgreSQL e uma tabela chamada `produtos` com a seguinte estrutura:

   ```sql
   CREATE TABLE produtos (
       id SERIAL PRIMARY KEY,
       nome VARCHAR(100),
       quantidade INTEGER,
       preco NUMERIC
   );
   ```


3. **Configuração das Credenciais**: No código, ajuste as variáveis `dbname`, `user` e `password` para corresponder às credenciais do seu banco de dados PostgreSQL.

4. **Execução do Programa**: Execute o script `main.py` para iniciar o sistema de gerenciamento de estoque.

## Observações

- Este projeto foi desenvolvido para fins educacionais e pode ser expandido com funcionalidades adicionais, como interface gráfica, autenticação de usuários e relatórios de vendas.
- Certifique-se de que o servidor PostgreSQL está em execução antes de iniciar o programa.
- Para ambientes de produção, considere implementar medidas de segurança, como a utilização de variáveis de ambiente para armazenar credenciais do banco de dados.


# Simulador de Avaliações em Python

- Este projeto teve sua origem e grande parte de seu desenvolvimento concebidos em um repositório anterior, de minha autoria, intitulado [Exercicios e Projetos em Python](https://github.com/LMolinaro01/Exercicios-e-Projetos-em-Python). O histórico de commits permanecem registrada neste repositório precursor, fornecendo um contexto para o desenvolvimento subsequente. Portanto, os marcos iniciais e a essência fundacional do projeto residem nesse repositório anterior, refletindo o processo criativo e a evolução do conceito até sua atual forma refinada. Entretanto, também está disponível em um repositório próprio intitulado [Sistema de Avaliações em Python](https://github.com/LMolinaro01/Simulador-de-Avaliacoes-em-Python)

## Execução do Programa:
  
<p align="center">
  <a href="https://www.youtube.com/watch?v=2irwlujDGsA" target = "_blank">
    <img src="https://github.com/LMolinaro01/Projetos-e-Exercicios-em-Python/assets/126402616/43966a60-b0f7-42aa-9a4a-ab3ca139baf7", width= 720px>
  </a>
</p>

---

O código fonte em Python representa um sistema que simula avaliações, oferecendo uma gama de funcionalidades essenciais para uma experiência de usuário completa e segura. Vou detalhar suas principais características e destacar suas medidas de segurança e validação:

1. **Banco de Dados SQLite com Prevenção contra SQL Injection**: Utilizando um banco de dados SQLite3, o programa armazena localmente informações, como dados dos alunos, senhas, questões da prova e pontuações. Além disso, implementa medidas eficazes para prevenir ataques de [*SQL Injection*](#sqlinjection), garantindo a integridade dos dados.

2. **Interface Gráfica com Tkinter**: Desenvolvido com [Tkinter](#tkinter), o programa oferece uma interface gráfica intuitiva e agradável, facilitando a interação do usuário em todas as etapas do processo, desde o cadastro até a visualização das pontuações.

3. **Cadastro Seguro com Validações**: A função de cadastro foi projetada com validações abrangentes para garantir a integridade dos dados. Além de evitar campos vazios, o sistema realiza verificações minuciosas para detectar e prevenir a inserção de caracteres especiais, protegendo contra possíveis vulnerabilidades como injeção de SQL.

4. **Cálculo Automático de Pontuações**: Após a conclusão da prova, o programa realiza o cálculo automático da pontuação do aluno, baseando-se nas respostas fornecidas de forma precisa e confiável.

5. **Exibição de Respostas e Gabaritos**: A exibição das respostas corretas e do gabarito é feita de maneira segura, garantindo que apenas os alunos autorizados tenham acesso a essas informações após a conclusão da prova. Além disso, há um passo a passo de como solucionar cada questão.

6. **Manipulação de Imagens com PIL**: Para uma experiência visual aprimorada, o programa utiliza a biblioteca [PIL](#pil) para manipular e exibir imagens, como o logo da instituição, garantindo uma apresentação visual atraente e profissional.

7. **Cadastro de Questões**: O código possui uma função que permite adicionar questões ao banco de dados.


Em resumo, este código implementa um sistema completo de simulador de avaliações, desde o cadastro de alunos até a realização e correção de provas, utilizando uma interface gráfica simples e agradável.

### Glossário:

- *SQL Injection*<a name="sqlinjection"></a>: é uma técnica maliciosa utilizada por hackers para explorar vulnerabilidades em sistemas de bancos de dados. Imagine que um banco de dados é como uma gaveta cheia de informações organizadas em fichas. Com o SQL Injection, um invasor consegue inserir códigos maliciosos, como se fossem notas falsas, na caixa de busca dessa gaveta. Assim, ele pode enganar o sistema e obter acesso não autorizado a dados confidenciais ou até mesmo manipular, editar ou excluir informações importantes. É como se alguém conseguisse acesso à sua gaveta de informações secretas, mexesse em papéis importantes e até mesmo adicionasse ou removesse alguns, tudo sem você perceber. Por isso, é essencial que os sistemas tenham medidas de segurança para prevenir esse tipo de ataque.

---

- *PIL*<a name="pil"></a>: (Python Imaging Library) é uma biblioteca de processamento de imagens para Python. Com o PIL, os desenvolvedores podem realizar uma ampla variedade de operações em imagens, como abrir, editar, converter formatos, redimensionar, cortar, aplicar filtros, entre outras. Essa biblioteca é especialmente útil para aplicações que lidam com manipulação de imagens, como processamento de fotos digitais, reconhecimento de padrões, processamento de documentos, entre outros. O PIL oferece uma interface fácil de usar para realizar essas operações de forma eficiente, permitindo aos desenvolvedores criar e personalizar imagens de maneira flexível e poderosa.
---

- *Tkinter*<a name="tkinter"></a>: Tkinter é uma biblioteca padrão do Python usada para criar interfaces gráficas de usuário (GUI). Com Tkinter, os desenvolvedores podem criar janelas, botões, caixas de texto e outros elementos de interface de forma intuitiva. É uma ferramenta versátil que simplifica o desenvolvimento de aplicativos com uma interface de usuário interativa. Tkinter fornece uma maneira eficiente de criar aplicativos desktop com Python, permitindo aos desenvolvedores concentrarem-se na lógica do programa enquanto a biblioteca cuida da apresentação visual.

---


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


#### Comandos para Procurar Algo:

* a -> Procura a Letra A  
* . -> Procura qualquer coisa (menos pular linha)  
* \d -> Procura um dígito (\D procura o que não for um dígito)  
* \w -> Alfanumérico (\W não alfanumérico)  
* [abc] -> Procura A, B ou C  
* \n -> Pular linha  
* \s -> Procura espaços (\S procura o que não for espaço)  
* [^abc] -> Procura qualquer caractere **exceto** A, B ou C  
* \b -> Delimita uma borda de palavra  
* ^ -> Indica o início da linha  
* $ -> Indica o final da linha  

#### Comandos para Determinar a Quantidade:

* "+" -> Pega o Máximo possível (1 a infinito)  
* "*" -> Pega o Máximo (zero a infinito)  
* "?" -> Pega **zero ou um** (torna algo opcional)  
* {n} -> Pega N coisas  
* {n,} -> Pega no mínimo **N** coisas  
* {n,m} -> Pega **de N a M** coisas  
* | -> Comando OU  

#### Comandos de Agrupamento:

* (?=...) -> Positive Lookahead  
* (?!...) -> Negative Lookahead  
* (?<=...) -> Positive Lookbehind  
* (?<!...) -> Negative Lookbehind  
* ( ) -> Agrupa  
* (?:...) -> Agrupa **sem capturar**

### Código Exemplo:

``` py

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
enderecos = re.findall(r'(?<=Endereço:\s*)(.+)', dados)
print("Endereços:", enderecos)

# Exibir os salários
salarios = re.findall(r'Valor dos serviços: R\$ (\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)', dados)
print("Salários:", salarios)

```

### Extração de Dados com Regex

Este script utiliza expressões regulares (regex) para extrair informações de uma string contendo dados, como nomes, datas de nascimento, endereços e valores de serviço.

#### 1. Extração de Nomes
```python
nomes = re.findall(r'(?<=Nome:)\s*([^\d\n]+?)\s*(?=Data nascimento|Data de nascimento|$)', dados)
```
- **`(?<=Nome:)`**: Procura por "Nome:", sem incluí-lo na captura.
- **`\s*`**: Ignora espaços após "Nome:".
- **`([^\d\n]+?)`**: Captura o nome, evitando números e quebras de linha.
- **`(?=Data nascimento|Data de nascimento|$)`**: Garante que a captura pare antes de "Data nascimento" ou o final da string.

#### 2. Extração de Datas de Nascimento
```python
regex_datas = r'(?<=Data nascimento:|data nascimento:|data de nascimento:|Data de Nascimento:)\s*(\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{2}|\d{2}-\d{2}-\d{2})'
datas_nascimento = re.findall(regex_datas, dados)
```
- **`(?<=Data nascimento:|data nascimento:|data de nascimento:|Data de Nascimento:)`**: Captura a data, considerando várias variações da frase "Data nascimento".
- **`\s*`**: Ignora espaços após a frase "Data nascimento".
- **`(\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{2}|\d{2}-\d{2}-\d{2})`**: Captura datas nos formatos `DD/MM/AAAA`, `DD-MM-AAAA`, `DD/MM/AA`, `DD-MM-AA`.

#### 3. Extração de Endereços
```python
enderecos = re.findall(r'(?<=Endereço:\s*)(.+)', dados)
```
- **`(?<=Endereço:\s*)`**: Captura o endereço após "Endereço:", ignorando os espaços.
- **`(.+)`**: Captura todo o conteúdo do endereço até o final da linha.

#### 4. Extração de Valores de Serviço
```python
salarios = re.findall(r'Valor dos serviços: R\$ (\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))', dados)
```
- **`Valor dos serviços: R\$`**: Procura valores monetários na moeda brasileira (R$).
- **`(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))`**: Captura valores como `1.200,00` ou `1200.00`.

---

Este script permite extrair informações específicas de uma string estruturada, utilizando expressões regulares para identificar e isolar dados como nomes, datas, endereços e valores.


Aqui está um exemplo de README para o seu exercício de **Extrator de Nota Fiscal**, sendo bem didático para ajudar outros usuários a entender como utilizar o código:

---

## **Extrator de Nota Fiscal<a name="nfpanda"></a>**

### **Objetivo**
Este projeto tem como objetivo extrair e processar os valores de "Valor Total" de notas fiscais digitais (em formato `.txt`). O programa analisa os arquivos de texto, encontra os valores totais e os organiza em uma tabela utilizando a biblioteca `Pandas`, com o valor formatado corretamente no padrão brasileiro de moeda (R$ XXX.XXX,XX).

Além disso, ele calcula o valor total somado de todas as notas fiscais e exibe essa soma de forma separada na tabela.

### **Como Funciona**

#### **1. Estrutura dos Arquivos**

Os arquivos `.txt` devem seguir um formato específico, onde o campo "Valor Total" está presente, como no exemplo abaixo:

```
Valor Total: R$ 200.000,00
```

O código irá procurar por esses valores dentro de cada arquivo, e formatar os valores de acordo com o padrão brasileiro.

#### **2. O que o Código Faz**

1. **Lê arquivos `.txt`**: O programa percorre todos os arquivos `.txt` na pasta onde o script está localizado.
2. **Extrai o valor de "Valor Total"**: Utilizando expressões regulares, o código encontra o valor da nota fiscal (ex: `R$ 200.000,00`).
3. **Formata os valores**: Converte os valores encontrados para o formato **R$ XXX.XXX,XX**.
4. **Cria uma tabela**: Utiliza a biblioteca `Pandas` para organizar os dados em uma tabela (DataFrame), incluindo o valor de cada nota e a soma total dos valores.
5. **Exibe e exporta**: Exibe a tabela no terminal e também a exporta para um arquivo CSV, se necessário.

#### **3. Estrutura da Tabela**

A tabela gerada será similar a esta:

| Arquivo       | Valor Total   |
|---------------|---------------|
| nota1.txt     | R$ 200.000,00 |
| nota2.txt     | R$ 150.000,00 |
| nota3.txt     | R$ 50.000,00  |
| **Total**     | **R$ 400.000,00** |

#### **4. Requisitos**

Antes de rodar o código, você precisa instalar as dependências necessárias:

- **Python 3.x**: Este código foi desenvolvido utilizando Python 3.x.
- **Pandas**: Biblioteca usada para manipulação de dados e geração da tabela.
  
Instale o **Pandas** com o seguinte comando:

```bash
pip install pandas
```

#### **5. Como Usar**

1. **Prepare os Arquivos `.txt`**: Coloque todos os arquivos `.txt` com as notas fiscais na mesma pasta onde está o script.
2. **Execute o Script**: Execute o script Python para processar as notas fiscais. O código vai procurar todos os arquivos `.txt`, extrair os valores de "Valor Total", formatá-los e gerar a tabela.

Para rodar o código:

```bash
python extrator_nf.py
```

3. **Verifique a Saída**: O código irá exibir a tabela com os valores das notas fiscais no terminal. Ele também salvará a tabela em um arquivo CSV, caso você deseje salvar os dados em um arquivo.

#### **6. Saída Esperada**

Ao rodar o código, a tabela será exibida da seguinte maneira:

```
            Arquivo      Valor Total
0       nota1.txt       R$ 200.000,00
1       nota2.txt       R$ 100.000,00
2       nota3.txt       R$ 50.000,00
3           Total       R$ 350.000,00
```

A tabela também será salva no arquivo `nota_fiscal_valores.csv` na mesma pasta.

#### **7. Personalização**

- Você pode ajustar a expressão regular no código caso o formato dos arquivos `.txt` mude.
- O script pode ser expandido para adicionar mais informações ou tratar mais dados conforme necessário.

---

### **Conclusão**

Este exercício é uma forma prática de trabalhar com:
- **Expressões regulares** para extração de dados específicos de arquivos.
- **Pandas** para organização e manipulação de dados.
- **Manipulação de arquivos** (leitura e escrita de arquivos `.txt` e `.csv`).

Agora você pode facilmente extrair valores de notas fiscais e calcular o total automaticamente 

---
<a name="guiaregex"></a>
# **Regex no Python: Guia Completo**  


## **Sumário**  
1. [Comandos de Busca](#comandos-de-busca)  
2. [Quantificadores](#quantificadores)  
3. [Agrupamento e Lookarounds](#agrupamento)  
4. [Exemplos Práticos](#exemplos)  
5. [Dicas para Uso no Python](#dicas)  

---

<a name="comandos-de-busca"></a>  
## **1. Comandos de Busca**  
Definem **o que** procurar em um texto.  

| **Comando** | **Descrição**                                                                 | **Exemplo**                                   |  
|-------------|-------------------------------------------------------------------------------|-----------------------------------------------|  
| `a`         | <span style="color: #EA4335">**Letra "a"**</span> (case-sensitive).           | Texto: `"Python"` → Nenhum match.             |  
| `.`         | <span style="color: #34A853">**Coringa**</span> (qualquer caractere exceto `\n`). | `r"P.th"` → Match em `"Pyth"` (`"y"` + `"th"`). |  
| `\d`        | <span style="color: #FBBC05">**Dígito**</span> (0-9). `\D` = não dígito.     | `"Python 3.10"` → Encontra `"3"`, `"1"`, `"0"`. |  
| `\w`        | <span style="color: #4285F4">**Alfanumérico**</span> (letras, números, `_`). | `"user_123"` → Match em `"user_123"`.         |  
| `[abc]`     | <span style="color: #EA4335">**Lista**</span> (a, b ou c).                   | `"Python"` → `r"[yt]"` encontra `"y"` e `"t"`. |  
| `\n`        | <span style="color: #34A853">**Quebra de linha**</span>.                     | Usado em textos multi-linha.                  |  
| `\s`        | <span style="color: #FBBC05">**Espaço em branco**</span> (espaço, tab, `\n`). | `"Python 3.10"` → Encontra o espaço.          |  
| `[^abc]`    | <span style="color: #4285F4">**Negação**</span> (exceto a, b, c).            | `"Python"` → `r"[^P]"` ignora `"P"`.          |  
| `\b`        | <span style="color: #EA4335">**Borda de palavra**</span>.                    | `r"\bPy"` → Match em `"Py"` de `"Python"`.    |  
| `^`         | <span style="color: #34A853">**Início da linha**</span>.                     | `r"^Py"` → Match se a linha começar com `"Py"`.|  
| `$`         | <span style="color: #FBBC05">**Fim da linha**</span>.                        | `r"10$"` → Match se terminar com `"10"`.      |  

---

<a name="quantificadores"></a>  
## **2. Quantificadores**  
Controlam **quantas vezes** um padrão aparece.  


| **Comando**  | **Descrição**                                                                 | **Exemplo** (Texto: `"123 4567"`)             |  
|-------------|-------------------------------------------------------------------------------|-----------------------------------------------|  
| `+`         | <span style="color: #EA4335">**1 ou mais**</span> (greedy).                  | `r"\d+"` → `"123"` e `"4567"`.               |  
| `*`         | <span style="color: #34A853">**0 ou mais**</span> (greedy).                  | `r"Py*"` → `"P"`, `"Py"`, `"Pyy"`.           |  
| `?`         | <span style="color: #FBBC05">**0 ou 1**</span> (opcional).                   | `r"Py?thon"` → `"Python"` ou `"Pthon"`.       |  
| `{n}`       | <span style="color: #4285F4">**Exatamente `n`**</span> ocorrências.          | `r"\d{3}"` → `"123"`.                        |  
| `{n,}`      | <span style="color: #EA4335">**No mínimo `n`**</span>.                       | `r"\d{4,}"` → `"4567"`.                      |  
| `{n,m}`     | <span style="color: #34A853">**Entre `n` e `m`**</span>.                     | `r"\d{2,4}"` → `"123"` e `"4567"`.           |  
| `|`         | <span style="color: #FBBC05">**OU lógico**</span>.                           | `r"cat|dog"` → `"cat"` ou `"dog"`.            |  
| `*?` / `+?` / `??` | <span style="color: #4285F4">**Quantificadores "lazy"**</span> (mínimo possível). | `r"\d+?"` → Match em `"1"`, `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"` (um por vez, não "123" nem "4567"). |  

---

<a name="agrupamento"></a>  
## **3. Agrupamento e Lookarounds**  
Agrupam padrões e adicionam lógica condicional.  

| **Comando**       | **Descrição**                                                                 | **Exemplo**                                   |  
|-------------------|-------------------------------------------------------------------------------|-----------------------------------------------|  
| `(?=...)`         | <span style="color: #4285F4">**Positive Lookahead**</span>: Padrão à frente.  | `r"\w+(?=@)"` → `"user"` em `"user@email.com"`. |  
| `(?!...)`         | <span style="color: #EA4335">**Negative Lookahead**</span>: Não deve existir. | `r"\d{3}(?!-)"` → Ignora `"123-"`.            |  
| `(?<=...)`        | <span style="color: #34A853">**Positive Lookbehind**</span>: Padrão antes.   | `r"(?<=\$)\d+"` → `"100"` em `"$100"`.        |  
| `(?<!...)`        | <span style="color: #FBBC05">**Negative Lookbehind**</span>: Não deve existir. | `r"(?<!-)\d+"` → Ignora `"-100"`.             |  
| `( )`             | <span style="color: #4285F4">**Grupo de captura**</span>.                    | `r"(\d{3})-(\d{4})"` → Grupos `"123"` e `"4567"`. |  
| `(?:...)`         | <span style="color: #EA4335">**Grupo não capturador**</span>.                | `r"(?:www\.)?(\w+)"` → Ignora `"www."`.       |  

---

## **Extra. Flags em Expressões Regulares**

A seguir, um guia completo e didático sobre os principais flags (modificadores) utilizados em expressões regulares, com exemplos e explicações detalhadas.

---

### 1. Introdução

Os flags são parâmetros que alteram o comportamento padrão das expressões regulares. Eles são adicionados logo após a barra final da regex (por exemplo, `/padrão/flags`) e permitem controlar como as buscas são realizadas, como a sensibilidade a maiúsculas/minúsculas, a forma de tratar quebras de linha e se a busca deve ser feita em toda a string.

---

### 2. Principais Flags e Seus Efeitos

| **Flag** | **Nome**              | **Descrição**                                                                                                                                                     | **Exemplo**                                             |
|----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `g`      | Global                | Procura por **todas** as ocorrências do padrão na string, em vez de parar no primeiro match encontrado.                                                           | `/a/g` em `"banana"` encontra todas as ocorrências de `"a"`. |
| `i`      | Case-insensitive      | Torna a busca **insensível a maiúsculas e minúsculas**. Por exemplo, `a` encontrará tanto `"a"` quanto `"A"`.                                                       | `/abc/i` em `"ABC"` encontra `"ABC"`.                   |
| `m`      | Multiline             | Modifica o comportamento de `^` (início da linha) e `$` (fim da linha) para que correspondam, respectivamente, ao início e fim de **cada linha** da string.   | `/^a/m` em `"abc\nabc"` encontra o `"a"` no início de cada linha. |
| `s`      | Dotall (Single-line)  | Faz com que o ponto (`.`) **corresponda a todos os caracteres**, incluindo quebras de linha (`\n`). Sem esse flag, o `.` não captura `\n`.                     | `/a.*b/s` em `"a\nb"` encontra o padrão mesmo com a quebra de linha. |
| `u`      | Unicode               | Permite que a expressão regular interprete corretamente **caracteres Unicode**. É importante para lidar com símbolos, acentos e emojis.                            | `/\u{1F600}/u` corresponde ao emoji 😀.                 |
| `y`      | Sticky                | Realiza a busca de forma **aderente** à posição indicada pela propriedade `lastIndex`. O regex só encontrará um match se este começar exatamente na posição indicada. | Em `"abca"`, usando `/a/y` com `lastIndex` definido em `0`, encontrará `"a"` somente se estiver na posição exata. |

---

### 3. Exemplos Práticos

#### 3.1. Flag `g` (Global)

Sem o flag `g`, a função de busca (como `match` em JavaScript) retorna apenas o primeiro match.  
```javascript
const texto = "banana";
console.log(texto.match(/a/));   // Resultado: ["a"]
console.log(texto.match(/a/g));  // Resultado: ["a", "a", "a"]
```

#### 3.2. Flag `i` (Case-insensitive)

Essa flag ignora as diferenças entre letras maiúsculas e minúsculas.  
```javascript
const texto = "Banana";
console.log(texto.match(/banana/));   // Resultado: null (não encontrou)
console.log(texto.match(/banana/i));  // Resultado: ["Banana"]
```

#### 3.3. Flag `m` (Multiline)

Quando uma string contém quebras de linha, `^` e `$` passam a funcionar em cada linha.  
```javascript
const texto = "primeira linha\nsegunda linha";
console.log(texto.match(/^segunda/m));  // Resultado: ["segunda"] (encontra "segunda" no início da segunda linha)
```

#### 3.4. Flag `s` (Dotall)

O ponto (`.`) passa a incluir as quebras de linha na captura.  
```javascript
const texto = "linha1\nlinha2";
console.log(texto.match(/linha.*linha/));   // Sem o flag `s`: null
console.log(texto.match(/linha.*linha/s));  // Com o flag `s`: ["linha1\nlinha2"]
```

#### 3.5. Flag `u` (Unicode)

Garante o tratamento correto de caracteres Unicode.  
```javascript
const texto = "😀";
console.log(texto.match(/\u{1F600}/));    // Sem `u`: pode não funcionar corretamente
console.log(texto.match(/\u{1F600}/u));   // Com `u`: ["😀"]
```

#### 3.6. Flag `y` (Sticky)

A busca "sticky" só considera matches que começam exatamente na posição definida por `lastIndex`.  
```javascript
const regex = /a/y;
const texto = "baaa";

// Tentativa sem ajustar lastIndex:
console.log(regex.exec(texto));   // Resultado: null, pois "a" não está na posição 0

// Ajustando lastIndex para 1:
regex.lastIndex = 1;
console.log(regex.exec(texto));   // Resultado: ["a"]
```

---

### 4. Conclusão

Cada flag tem um papel específico na forma como a expressão regular interpreta e pesquisa um texto:

- **`g`**: Encontra todas as ocorrências.
- **`i`**: Ignora diferenças entre maiúsculas e minúsculas.
- **`m`**: Permite que `^` e `$` atuem em cada linha, não apenas na string completa.
- **`s`**: Permite que o ponto (`.`) capture quebras de linha.
- **`u`**: Ativa o suporte a caracteres Unicode, essencial para textos com acentos, emojis e símbolos especiais.
- **`y`**: Realiza a busca de forma estrita a partir da posição atual.


<a name="exemplos"></a>  
## **4. Exemplos Práticos**  

### **Exemplo 1: Validar E-mail**  
```python  
import re  
email = "user_123@domain.com"  
padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"  
if re.match(padrao, email):  
    print("Válido!")  
```  
**Funcionamento**:  
1. `^[\w\.-]+`: Nome do usuário (permite letras, números, `.`, `-`, `_`).  
2. `@[\w\.-]+`: Domínio (ex: `gmail`, `hotmail`).  
3. `\.\w+$`: Extensão (ex: `.com`, `.org`).  

---

### **Exemplo 2: Extrair Datas**  
```python  
texto = "Data: 25/12/2023"  
padrao = r"\b(\d{2})/(\d{2})/(\d{4})\b"  
match = re.search(padrao, texto)  
if match:  
    dia, mes, ano = match.groups()  # ("25", "12", "2023")  
```  

---

### **Exemplo 3: Senha Forte**  
```python  
senha = "Senha@123"  
padrao = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"  
if re.match(padrao, senha):  
    print("Senha segura!")  
```  
**Regras**:  
- Mínimo 8 caracteres.  
- Pelo menos uma letra maiúscula, um número e um caractere especial.  

---

<a name="dicas"></a>  
## **5. Dicas para Uso no Python**  

**Use raw strings**: Evite conflitos com `\` usando `r"..."`.  
```python  
re.search(r"\d+", texto)  # Correto  
re.search("\d+", texto)   # Erro (use raw string)!  
```  

 **Funções úteis**:  
- `re.findall()`: Retorna todas as ocorrências.  
- `re.sub()`: Substitui partes do texto.  

 **Teste online**: Use ferramentas como [Regex101](https://regex101.com/) para validar padrões.  

---

<a name="gatofato"></a>
## CatFactApp - Aplicativo de Fatos sobre Gatos

Simples aplicativo desenvolvido com `customtkinter` para exibir fatos sobre gatos. Ele faz chamadas para APIs externas para obter um fato aleatório sobre gatos e traduzi-lo para português.

https://github.com/user-attachments/assets/3a32be2d-8ac2-4a66-94a4-99499c8e1b63

### Tecnologias Utilizadas
- `customtkinter`: Para criar a interface gráfica moderna em Python.
- `requests`: Para fazer requisições HTTP e buscar os dados das APIs.
- `re` (expressões regulares): Para extrair os fatos da resposta da API.
- `API catfact.ninja`: Fornece fatos aleatórios sobre gatos.
- `API MyMemory`: Traduz textos automaticamente.

### Como Funciona
1. O aplicativo inicia com um botão que, quando pressionado, busca um fato aleatório sobre gatos da API `catfact.ninja`.
2. O fato retornado está em inglês e é extraído do JSON usando expressões regulares (`re.search`).
3. O texto é enviado para a API de tradução `MyMemory` para ser convertido para português.
4. O fato traduzido é exibido na interface do aplicativo.

### O que é uma API?
API (“Application Programming Interface”) é um conjunto de regras que permite que um software interaja com outro. No nosso caso:
- **API catfact.ninja** retorna um fato sobre gatos em inglês.
- **API MyMemory** recebe um texto e devolve a tradução para português.

### O que é uma Expressão Regular (Regex)?
Regex (“expressões regulares”) é uma forma de buscar padrões em textos. No nosso código, usamos `re.search(r'"fact":"(.*?)"', response.text)` para encontrar o fato retornado pela API.

### Testando com Postman
[Postman](https://www.postman.com/) é uma ferramenta para testar APIs. Para testar a API manualmente:
1. Abra o Postman.
2. Insira `https://catfact.ninja/fact` no campo de URL.
3. Clique em "Send" e veja a resposta JSON com um fato sobre gatos.

Se quiser testar a tradução:
1. Use a URL `https://api.mymemory.translated.net/get`.
2. Configure o parâmetro `q` com o texto e `langpair` com `en|pt`.
3. Envie a requisição e verifique a tradução na resposta.


---



### **Portifólio**

https://tinyurl.com/5dpr33pv
