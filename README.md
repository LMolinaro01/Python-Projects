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
* [Spark - Processamento e Análise de Dados com Distribuição Normal](#sparknormal)

### Automação e Manipulação de Arquivos

* [UnifyFiles - Organizador de Arquivos em Pasta Principal](#)
* [PDF Merger - Unificador de Arquivos PDF](#)
* [MKV Subtitle Picker - Extrator de Legendas de Arquivos MKV](#)
* [Selenium - Pesquisa na Wikipédia](#seleniumwiki)
* [Sensor de LDR integrado com Python](https://github.com/LMolinaro01/Arduino-Projects)

### Outros

* [UV - Package Manager + ChatGPT com Langchain](#uv)
* [UV - Package Manager Explicação](#uv2)
* [Design Patterns em Python](#design-pattern)

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

<a name="sparknormal"></a>

## Spark - Processamento e Análise de Dados com Distribuição Normal

Exemplo prático de configuração do Apache Spark para análise de dados gerados a partir de uma distribuição normal. Este projeto demonstra como integrar `numpy`, `pandas` e `pyspark` para gerar, processar e consultar grandes volumes de dados de maneira eficiente.


### Tecnologias Utilizadas
- **openjdk-8-jdk-headless**: Necessário para executar o Apache Spark.
- **Apache Spark**: Framework de processamento distribuído para análise de big data.
- **findspark**: Permite que o Python encontre e configure a instalação do Spark.
- **pyspark**: API do Spark para Python, utilizada para criar sessões e DataFrames.
- **numpy**: Para gerar dados com distribuição normal.
- **pandas**: Para manipulação e conversão de dados entre DataFrames.

### Como Funciona
1. **Instalação e Configuração**:
   - Instala o Java 8, essencial para a execução do Spark.
   - Baixa e descompacta o Apache Spark (versão 3.5.5 com suporte Hadoop3).
   - Instala as bibliotecas `findspark` e `pyspark`, preparando o ambiente Python para trabalhar com Spark.
   - Define as variáveis de ambiente `JAVA_HOME` e `SPARK_HOME` para que o Spark seja corretamente localizado pelo sistema.

2. **Geração de Dados**:
   - Utiliza o `numpy` para gerar 10.000 amostras de uma distribuição normal com média 0 e desvio padrão 0.1.
   - Cria um DataFrame do `pandas` com esses dados, facilitando a manipulação inicial.

3. **Integração com Spark**:
   - Converte o DataFrame do `pandas` para um DataFrame do Spark.
   - Registra o DataFrame como uma tabela temporária no Spark, permitindo consultas SQL.

4. **Consulta e Validação**:
   - Executa uma consulta SQL para contar quantos valores da coluna estão no intervalo entre -0.1 e 0.1.
   - Este intervalo corresponde a aproximadamente 68% dos dados, validando uma propriedade fundamental da distribuição normal.
   - Converte o resultado da consulta para um DataFrame do `pandas` para visualização e análise.

### O que é Apache Spark?
O Apache Spark é um poderoso framework de computação distribuída que facilita o processamento de grandes volumes de dados com alta performance. Ele é amplamente utilizado em ambientes de big data para tarefas como processamento em lote, streaming, machine learning e análise interativa.

### O que é Distribuição Normal?
A Distribuição Normal é uma das distribuições estatísticas mais importantes, caracterizada por uma curva em forma de sino. Ela é definida por dois parâmetros:
- **Média (μ)**: Centraliza os dados.
- **Desvio Padrão (σ)**: Determina a dispersão dos dados.
No contexto deste projeto, aproximadamente 68% dos valores gerados estão dentro de 1 desvio padrão da média (entre -0.1 e 0.1), o que é verificado pela consulta SQL.

![image](https://github.com/user-attachments/assets/a7bbe2cc-f70a-4a47-abc7-16435cecf2e6)

### Considerações sobre o Comportamento dos Dados
Caso os dados não se comportem como esperado para uma distribuição normal — por exemplo, se a contagem dos valores no intervalo entre -0.1 e 0.1 não estiver próxima de 68% dos dados totais — pode indicar que há algo errado com o conjunto de dados.
Possíveis causas para esse comportamento atípico incluem:

- Fraude: Manipulação intencional dos dados para distorcer a análise.

- Omissão de Dados: Dados importantes podem ter sido ignorados ou não coletados corretamente.

- Perda de Dados: Problemas no processo de coleta ou armazenamento podem ter levado à perda de registros.

- Erros de Processamento: Inconsistências durante a conversão ou manipulação dos dados entre pandas e Spark.

Esses sinais podem levar a conclusões estatísticas incorretas e impactar a qualidade da análise, sendo fundamental identificar e corrigir esses problemas para garantir a integridade dos resultados.

### Testando o Código
Para testar o funcionamento:
1. Execute os comandos para instalar o Java, baixar e configurar o Spark, e instalar as dependências necessárias.
2. Configure as variáveis de ambiente para `JAVA_HOME` e `SPARK_HOME`.
3. Execute o script Python que gera os dados, converte para Spark DataFrame, cria a tabela temporária e realiza a consulta SQL.
4. Verifique o resultado: a contagem dos valores no intervalo deve ser próxima de 6800, confirmando a propriedade da distribuição normal.

---

Este projeto demonstra uma abordagem eficiente para integração entre bibliotecas de manipulação de dados e ferramentas de processamento distribuído, facilitando a análise estatística em escala.

<a name="seleniumwiki"></a>

# Automação com Selenium - Pesquisa na Wikipédia

Exemplo prático de automação utilizando o **Selenium** para realizar uma pesquisa automatizada na **Wikipédia**. O projeto mostra como controlar o navegador de forma programática para simular uma pesquisa do termo **"Engenharia de Software"** na Wikipédia, utilizando a biblioteca **Selenium** com Python.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada para o script de automação.
- **Selenium**: Biblioteca de automação de navegadores que permite controlar um navegador da web, como o Google Chrome, para simular interações de um usuário real.
- **Google Chrome**: Navegador utilizado no projeto.
- **ChromeDriver**: Driver necessário para o Selenium interagir com o navegador Google Chrome.

## Como Funciona

1. **Instalação e Configuração**:
   - Instale o Python 3.x em sua máquina, caso ainda não tenha.
   - Instale o Selenium, que é a biblioteca principal utilizada para controlar o navegador. Você pode instalá-la com o seguinte comando:

     ```bash
     pip install selenium
     ```

   - Baixe o **ChromeDriver** (versão correspondente ao seu navegador Chrome) em [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/). Após o download, extraia o arquivo e adicione o caminho ao `PATH`, ou forneça o caminho completo no código.

2. **O Script**:
   - O código abre o navegador Google Chrome e acessa a página inicial da Wikipédia.
   - Em seguida, localiza o campo de pesquisa da Wikipédia e insere o termo **"Engenharia de Software"**.
   - O script pressiona **ENTER** para realizar a pesquisa.
   - Após carregar a página de resultados, o script salva uma captura de tela com o nome `screenshot.png`.
   - Por fim, o navegador é fechado.

3. **Executando o Script**:
   - Após configurar o ambiente, salve o código em um arquivo `pesquisa_wikipedia.py`.
   - Execute o script no terminal:

     ```bash
     python pesquisa_wikipedia.py
     ```

   - O navegador será aberto automaticamente, realizará a pesquisa e salvará a captura de tela.

https://github.com/user-attachments/assets/90541ea8-e1ca-4773-ba1d-d89bc95a046e

## O que é Selenium?

O **Selenium** é uma biblioteca de automação de testes de código aberto que permite controlar navegadores da web. Ele é amplamente utilizado para testar interfaces de usuário de aplicações web, mas também pode ser usado para automação de tarefas repetitivas como preencher formulários, fazer buscas em sites e navegar entre páginas, exatamente como um usuário faria manualmente.

No contexto deste projeto, o Selenium é utilizado para simular a pesquisa na Wikipédia, o que facilita a interação com páginas web sem a necessidade de um usuário manual.

## Testando o Código

1. **Instalar as Dependências**: Instale o Python e o Selenium, e faça o download do **ChromeDriver** para a versão do seu Google Chrome.
2. **Executar o Script**: Execute o script Python com o comando mencionado anteriormente. O navegador será aberto, o termo "Engenharia de Software" será pesquisado na Wikipédia e uma captura de tela da página de resultados será salva como `screenshot.png`.
3. **Verifique o Resultado**: Após a execução, verifique o arquivo `screenshot.png` para confirmar que a pesquisa foi realizada corretamente.

## Considerações Finais

Este projeto mostra como utilizar o Selenium para automatizar a interação com uma página web, neste caso, realizando uma pesquisa na Wikipédia. A capacidade de automatizar interações com páginas web pode ser útil para diversas finalidades, como testes de software, scraping de dados e automação de tarefas repetitivas.

Com o Selenium, é possível simular quase qualquer ação de um usuário, o que torna essa ferramenta muito poderosa para automação de navegadores.

---

# ChatGPT com LangChain e `uv` 
<a name="uv"> </a>

Este é um projeto simples que utiliza o modelo `gpt-4o` da OpenAI via `LangChain`, com gerenciamento de dependências feito pelo poderoso gerenciador de pacotes [`uv`](https://docs.astral.sh/uv/).

---

## Sobre o Projeto

O script realiza uma pergunta via terminal ao usuário e envia essa entrada para o modelo `gpt-4o`, retornando uma resposta gerada por IA.

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

pergunta = input("O Que deseja saber?: ")
resposta = llm.invoke(str(pergunta))

print(resposta.content)
````

---

## Requisitos

* Python 3.8+
* Git Bash (ou outro terminal compatível no Windows)
* Conexão com a internet
* Uma chave de API da OpenAI (armazenada em um arquivo `.env`)

---

## Instalação do `uv`

[`uv`](https://docs.astral.sh/uv/) é um gerenciador de pacotes moderno, rápido e eficiente criado pela [Astral](https://astral.sh). Ele substitui `pip`, `virtualenv` e `pip-tools` com uma única ferramenta.

### 1. Instalar o `uv`

No terminal (ex: Git Bash), execute:

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

Se necessário, adicione `uv` ao seu PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verifique se funcionou:

```bash
uv --version
```

---

### 2. Inicializar o projeto com `uv`

Crie o ambiente virtual e configure o projeto:

```bash
uv init .
```

---

### 3. Adicionar as dependências

Adicione os pacotes necessários:

```bash
uv add python-dotenv
uv add langchain-openai
```

> Obs: `python-dotenv` carrega variáveis do `.env`; `langchain-openai` integra com a API da OpenAI.

---

### 4. Criar o arquivo `.env`

Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 5. Rodar o projeto

Execute o script com:

```bash
uv run main.py
```

---

## Documentação oficial do `uv`

Acesse a documentação completa aqui:
🔗 [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

## Exemplos de uso

```bash
$ uv add requests
$ uv remove numpy
$ uv sync
$ uv pip freeze
```

---

## Benefícios de usar `uv`

* Ultra-rápido (usa Rust)
* Substitui `pip`, `venv` e `pip-tools`
* Sincronização automática de ambientes
* Cache inteligente de pacotes

---

# UV — Novo Gerenciador de Pacotes Python

<a name="uv2"> </a>

![image](https://github.com/user-attachments/assets/ecb08e2d-b7b7-4b06-8e66-984f07b4202d)

`uv` é um gerenciador de pacotes e ambientes para Python, desenvolvido em Rust pela Astral, que unifica e substitui `pip`, `venv`, `pip-tools` e arquivos de lock fragmentados. Ele oferece instalação rápida, lock determinístico e workflow simplificado.

---

## Instalação

1. Baixe e execute o instalador:
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | bash


2. (Opcional) Adicione ao seu PATH, se o comando não for reconhecido:

   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

3. Verifique a instalação:

   ```bash
   uv --version
   # Exemplo de saída: uv 0.7.4 (6fbcd09b5 2025-05-15)
   ```

---

## Fluxo Básico de Uso

1. **Inicializar projeto**

   ```bash
   cd meu-projeto
   uv init .
   ```

   * Cria um ambiente virtual em `./.venv/`
   * Gera `uv.lock` com todas as dependências atuais

2. **Adicionar dependências**

   ```bash
   uv add <pacote>[@<versão>]
   ```

   * Exemplo: `uv add requests`
   * Resolve versões, instala no venv e atualiza `uv.lock`

3. **Remover pacotes**

   ```bash
   uv remove <pacote>
   ```

   * Remove do venv e atualiza `uv.lock`

4. **Sincronizar ambiente**

   ```bash
   uv sync
   ```

   * Garante que o venv reflita exatamente o conteúdo de `uv.lock`

5. **Executar scripts**

   ```bash
   uv run python main.py
   ```

   * Executa o script dentro do ambiente isolado
   * Também funciona com shebang: `uv run ./script.py`

---

## Lock Determinístico

* Todas as dependências diretas e transitivas são travadas em `uv.lock`.
* Ambientes reprodutíveis em diferentes máquinas com o mesmo arquivo de lock.

---

## Benefícios

| Característica        | Descrição                                             |
| --------------------- | ----------------------------------------------------- |
| Performance em Rust   | Instalações e resolução de dependências muito rápidas |
| Tudo em um            | Substitui diversas ferramentas em uma única CLI       |
| Standalone            | Não exige `pip install uv` em um ambiente Python      |
| Lock completo         | Trava tanto dependências diretas quanto indiretas     |
| Workflow simplificado | Comandos `init`, `add`, `remove`, `sync`, `run`       |

---

## Documentação Oficial

Consulte o guia completo em:
[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

<a name = "design-pattern"> </a>
# Design Patterns (Padrões de Projetos) 

## Criação

### 1. **Abstract Factory**

O padrão **Abstract Factory** fornece uma interface para criar famílias de objetos relacionados, sem especificar suas classes concretas. Ou seja, ele permite criar diferentes tipos de objetos (produtos) relacionados de uma maneira independente da implementação concreta desses objetos.

#### Exemplo em Python:

```python
# Produtos concretos
class ProdutoA1:
    def operacao(self):
        return "ProdutoA1 operando"

class ProdutoA2:
    def operacao(self):
        return "ProdutoA2 operando"

class ProdutoB1:
    def operacao(self):
        return "ProdutoB1 operando"

class ProdutoB2:
    def operacao(self):
        return "ProdutoB2 operando"

# Fábrica abstrata
class FábricaAbstrata:
    def criar_produto_a(self):
        raise NotImplementedError
    
    def criar_produto_b(self):
        raise NotImplementedError

# Fábricas concretas
class FábricaConcreta1(FábricaAbstrata):
    def criar_produto_a(self):
        return ProdutoA1()
    
    def criar_produto_b(self):
        return ProdutoB1()

class FábricaConcreta2(FábricaAbstrata):
    def criar_produto_a(self):
        return ProdutoA2()
    
    def criar_produto_b(self):
        return ProdutoB2()

# Cliente
def cliente(fábrica: FábricaAbstrata):
    produto_a = fábrica.criar_produto_a()
    produto_b = fábrica.criar_produto_b()
    print(produto_a.operacao())
    print(produto_b.operacao())

# Testando
fábrica1 = FábricaConcreta1()
cliente(fábrica1)

fábrica2 = FábricaConcreta2()
cliente(fábrica2)
```

### 2. **Builder**

O **Builder** separa a construção de um objeto complexo da sua representação, permitindo criar diferentes representações do mesmo tipo de objeto. Ele é usado quando você precisa construir um objeto com várias partes, mas não quer que o cliente tenha que lidar com a complexidade de montar o objeto por si só.

#### Exemplo em Python:

```python
class Produto:
    def __init__(self):
        self.partes = []
    
    def adicionar_parte(self, parte):
        self.partes.append(parte)

    def __str__(self):
        return "Produto com partes: " + ", ".join(self.partes)

# Builder
class Construtor:
    def __init__(self):
        self.produto = Produto()

    def construir_parte_1(self):
        self.produto.adicionar_parte("Parte 1")

    def construir_parte_2(self):
        self.produto.adicionar_parte("Parte 2")

    def construir_parte_3(self):
        self.produto.adicionar_parte("Parte 3")

    def get_produto(self):
        return self.produto

# Diretor
class Diretor:
    def __init__(self, construtor):
        self.construtor = construtor

    def construir(self):
        self.construtor.construir_parte_1()
        self.construtor.construir_parte_2()

# Testando
construtor = Construtor()
diretor = Diretor(construtor)
diretor.construir()
produto = construtor.get_produto()
print(produto)
```

### 3. **Factory Method**

O **Factory Method** define um método que cria objetos em uma superclasse, mas permite que subclasses alterem o tipo de objetos que serão criados. Ele delega a responsabilidade de instanciar as classes concretas para as subclasses, sem que o cliente precise saber qual é a classe exata.

#### Exemplo em Python:

```python
from abc import ABC, abstractmethod

# Produto
class Produto(ABC):
    @abstractmethod
    def operacao(self):
        pass

class ProdutoConcretoA(Produto):
    def operacao(self):
        return "Operação A"

class ProdutoConcretoB(Produto):
    def operacao(self):
        return "Operação B"

# Criador
class Criador(ABC):
    @abstractmethod
    def criar_produto(self):
        pass

# Criadores concretos
class CriadorConcretoA(Criador):
    def criar_produto(self):
        return ProdutoConcretoA()

class CriadorConcretoB(Criador):
    def criar_produto(self):
        return ProdutoConcretoB()

# Cliente
def cliente(criador: Criador):
    produto = criador.criar_produto()
    print(produto.operacao())

# Testando
criador_a = CriadorConcretoA()
cliente(criador_a)

criador_b = CriadorConcretoB()
cliente(criador_b)
```

### 4. **Prototype**

O **Prototype** permite a criação de novos objetos copiando um objeto existente, ao invés de criar novos objetos do zero. Ele é útil quando a criação de um novo objeto é cara, então, ao invés de criar um novo, você clona um objeto existente.

#### Exemplo em Python:

```python
import copy

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"Produto {self.nome} - {self.valor}"

    # Método de clonagem (Prototype)
    def clonar(self):
        return copy.deepcopy(self)

# Criando o protótipo
produto_original = Produto("Produto1", 100)

# Clonando o produto
produto_clone = produto_original.clonar()
produto_clone.nome = "Produto Clonado"
produto_clone.valor = 150

print(produto_original)
print(produto_clone)
```

### 5. **Singleton**

O **Singleton** garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a essa instância. Isso é útil quando você precisa garantir que exista apenas uma instância de uma classe, como no caso de um gerenciador de configuração global.

#### Exemplo em Python:

```python
class Singleton:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia

# Testando o Singleton
objeto1 = Singleton()
objeto2 = Singleton()

print(objeto1 is objeto2)  # True, ambas as instâncias são a mesma
```

### Resumo dos Padrões:

* **Abstract Factory**: Cria famílias de objetos relacionados sem especificar suas classes concretas.
* **Builder**: Separa a construção de um objeto complexo da sua representação.
* **Factory Method**: Cria objetos em uma superclasse, mas permite que subclasses alterem o tipo de objeto.
* **Prototype**: Cria novos objetos clonando objetos existentes.
* **Singleton**: Garante que uma classe tenha apenas uma instância.

---

## Estrutura

Claro! Vou explicar agora os padrões de **estrutura** e dar exemplos em Python para cada um deles.

### 1. **Adapter**

O padrão **Adapter** é usado para adaptar uma interface de uma classe para que ela possa ser utilizada em uma outra classe. Em outras palavras, ele permite que classes com interfaces incompatíveis possam trabalhar juntas.

#### Exemplo em Python:

```python
# Classe que precisa ser adaptada
class SistemaAntigo:
    def operar_antigo(self):
        return "Operação do Sistema Antigo"

# Classe que espera a interface nova
class SistemaNovo:
    def operar_novo(self):
        return "Operação do Sistema Novo"

# Adapter que adapta a interface
class Adapter(SistemaNovo):
    def __init__(self, sistema_antigo):
        self.sistema_antigo = sistema_antigo

    def operar_novo(self):
        return self.sistema_antigo.operar_antigo()

# Cliente
sistema_antigo = SistemaAntigo()
adapter = Adapter(sistema_antigo)
print(adapter.operar_novo())  # Adaptando para a interface nova
```

### 2. **Bridge**

O padrão **Bridge** desacopla uma abstração de sua implementação, permitindo que ambas possam variar independentemente. Ele é útil quando você tem várias implementações de uma abstração e quer desacoplar as mudanças nas implementações das mudanças nas abstrações.

#### Exemplo em Python:

```python
# Abstração
class Abstracao:
    def __init__(self, implementacao):
        self.implementacao = implementacao

    def operacao(self):
        raise NotImplementedError

# Implementação
class Implementacao:
    def operacao_impl(self):
        raise NotImplementedError

# Implementação Concreta A
class ImplementacaoA(Implementacao):
    def operacao_impl(self):
        return "Implementação A"

# Implementação Concreta B
class ImplementacaoB(Implementacao):
    def operacao_impl(self):
        return "Implementação B"

# Abstração Concreta
class AbstracaoConcreta(Abstracao):
    def operacao(self):
        return f"Operação com {self.implementacao.operacao_impl()}"

# Testando
implementacao_a = ImplementacaoA()
abstracao_a = AbstracaoConcreta(implementacao_a)
print(abstracao_a.operacao())  # "Operação com Implementação A"

implementacao_b = ImplementacaoB()
abstracao_b = AbstracaoConcreta(implementacao_b)
print(abstracao_b.operacao())  # "Operação com Implementação B"
```

### 3. **Composite**

O padrão **Composite** permite que objetos individuais e compostos sejam tratados de forma uniforme. Ele cria uma árvore de objetos em que cada nó pode ser um objeto simples ou composto. Isso é útil quando você tem hierarquias de objetos.

#### Exemplo em Python:

```python
from abc import ABC, abstractmethod

# Componente
class Componente(ABC):
    @abstractmethod
    def operação(self):
        pass

# Folha
class Folha(Componente):
    def operação(self):
        return "Folha"

# Composto
class Composto(Componente):
    def __init__(self):
        self.componentes = []

    def adicionar(self, componente: Componente):
        self.componentes.append(componente)

    def operação(self):
        return ", ".join([componente.operação() for componente in self.componentes])

# Testando
folha1 = Folha()
folha2 = Folha()
composto = Composto()
composto.adicionar(folha1)
composto.adicionar(folha2)

print(composto.operação())  # "Folha, Folha"
```

### 4. **Decorator**

O padrão **Decorator** permite adicionar funcionalidades a um objeto de forma dinâmica, sem alterar a classe original. Ele é útil quando você quer adicionar comportamentos extras a objetos em tempo de execução.

#### Exemplo em Python:

```python
class Produto:
    def custo(self):
        return 10

class Decorador(Produto):
    def __init__(self, produto):
        self.produto = produto

class DecoradorComDesconto(Decorador):
    def custo(self):
        return self.produto.custo() * 0.9  # Aplica desconto de 10%

class DecoradorComImposto(Decorador):
    def custo(self):
        return self.produto.custo() * 1.2  # Aplica imposto de 20%

# Testando
produto = Produto()
produto_com_desconto = DecoradorComDesconto(produto)
produto_com_imposto = DecoradorComImposto(produto_com_desconto)

print(produto_com_imposto.custo())  # Produto com 10% de desconto e 20% de imposto
```

### 5. **Facade**

O padrão **Facade** fornece uma interface unificada e simplificada para um conjunto de interfaces em um subsistema, facilitando o uso complexo dessas interfaces. Ele oculta as complexidades do subsistema para o cliente.

#### Exemplo em Python:

```python
class SubSistemaA:
    def operação_a(self):
        return "Operação A"

class SubSistemaB:
    def operação_b(self):
        return "Operação B"

class SubSistemaC:
    def operação_c(self):
        return "Operação C"

# Facade
class Facade:
    def __init__(self):
        self.a = SubSistemaA()
        self.b = SubSistemaB()
        self.c = SubSistemaC()

    def operação_facade(self):
        return f"{self.a.operação_a()}, {self.b.operação_b()}, {self.c.operação_c()}"

# Testando
facade = Facade()
print(facade.operação_facade())  # Chama o sistema de maneira simplificada
```

### 6. **Flyweight**

O padrão **Flyweight** permite compartilhar objetos para suportar grandes quantidades de objetos de forma eficiente, economizando memória. Ele é útil quando você tem muitas instâncias de um objeto que possuem partes de seu estado em comum.

#### Exemplo em Python:

```python
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

# Flyweight Factory
class CarroFactory:
    _carros = {}

    @staticmethod
    def get_carro(modelo):
        if modelo not in CarroFactory._carros:
            CarroFactory._carros[modelo] = Carro(modelo, "Branco")
        return CarroFactory._carros[modelo]

# Testando
carro1 = CarroFactory.get_carro("Fusca")
carro2 = CarroFactory.get_carro("Fusca")

print(carro1 is carro2)  # True, ambos são a mesma instância
```

### 7. **Proxy**

O padrão **Proxy** fornece um substituto ou representante de um objeto real. Ele pode ser utilizado para controlar o acesso a um objeto, por exemplo, para adicionar segurança, controle de acesso, ou até mesmo para carregar objetos pesados de forma preguiçosa.

#### Exemplo em Python:

```python
class RealSubject:
    def request(self):
        return "Pedido real feito"

# Proxy
class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Verificando permissão para fazer o pedido...")
        return self.real_subject.request()

# Testando
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())  # Proxy verifica antes de fazer o pedido real
```

---

### Resumo dos Padrões Estruturais:

* **Adapter**: Converte a interface de uma classe para outra, permitindo que interfaces incompatíveis trabalhem juntas.
* **Bridge**: Desacopla a abstração da implementação, permitindo variações independentes de ambos.
* **Composite**: Permite tratar objetos compostos e objetos simples de forma uniforme, formando uma estrutura hierárquica.
* **Decorator**: Adiciona funcionalidades adicionais a um objeto sem modificar sua estrutura.
* **Facade**: Simplifica o uso de um subsistema complexo fornecendo uma interface única.
* **Flyweight**: Compartilha objetos comuns para economizar memória quando você tem muitas instâncias similares.
* **Proxy**: Fornece um substituto ou representante de outro objeto, controlando o acesso ao objeto real.

## Comportamento

Claro! Vou explicar os padrões de **comportamento** e dar exemplos em Python para cada um deles. Esses padrões são fundamentais para definir como objetos interagem uns com os outros e gerenciam suas responsabilidades. Vamos a eles:

### 1. **Chain of Responsibility**

O padrão **Chain of Responsibility** permite que múltiplos objetos tratem uma solicitação, sem que o remetente saiba qual objeto irá tratar a solicitação. A solicitação é passada ao longo de uma cadeia de objetos, até que um deles consiga tratá-la.

#### Exemplo em Python:

```python
class Requisicao:
    def __init__(self, valor):
        self.valor = valor

class Manipulador:
    def __init__(self, proximo=None):
        self.proximo = proximo

    def manipular(self, requisicao):
        if self.proximo:
            return self.proximo.manipular(requisicao)
        return None

class ManipuladorA(Manipulador):
    def manipular(self, requisicao):
        if requisicao.valor <= 10:
            return f"Manipulado por A: {requisicao.valor}"
        return super().manipular(requisicao)

class ManipuladorB(Manipulador):
    def manipular(self, requisicao):
        if requisicao.valor <= 20:
            return f"Manipulado por B: {requisicao.valor}"
        return super().manipular(requisicao)

# Testando
requisicao = Requisicao(15)
manipulador = ManipuladorA(ManipuladorB())
print(manipulador.manipular(requisicao))  # Manipulado por B: 15
```

### 2. **Command**

O padrão **Command** encapsula uma solicitação como um objeto, permitindo parametrizar clientes com diferentes solicitações, enfileirar ou registrar solicitações, e suportar a execução de operações de forma remota.

#### Exemplo em Python:

```python
class Comando:
    def executar(self):
        pass

class ComandoConcretoA(Comando):
    def __init__(self, receptor):
        self.receptor = receptor

    def executar(self):
        return self.receptor.acao_a()

class ComandoConcretoB(Comando):
    def __init__(self, receptor):
        self.receptor = receptor

    def executar(self):
        return self.receptor.acao_b()

class Receptor:
    def acao_a(self):
        return "Ação A executada"

    def acao_b(self):
        return "Ação B executada"

class Invocador:
    def __init__(self):
        self.comandos = []

    def adicionar_comando(self, comando):
        self.comandos.append(comando)

    def executar_comandos(self):
        for comando in self.comandos:
            print(comando.executar())

# Testando
receptor = Receptor()
comando_a = ComandoConcretoA(receptor)
comando_b = ComandoConcretoB(receptor)

invocador = Invocador()
invocador.adicionar_comando(comando_a)
invocador.adicionar_comando(comando_b)

invocador.executar_comandos()
```

### 3. **Interpreter**

O padrão **Interpreter** fornece uma maneira de avaliar a gramática ou expressão de uma linguagem. Ele é útil quando você precisa interpretar ou compilar expressões dentro de uma linguagem específica.

#### Exemplo em Python:

```python
class Expressao:
    def interpretar(self):
        pass

class Numero(Expressao):
    def __init__(self, numero):
        self.numero = numero

    def interpretar(self):
        return self.numero

class Soma(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def interpretar(self):
        return self.esquerda.interpretar() + self.direita.interpretar()

# Testando
num1 = Numero(5)
num2 = Numero(10)
soma = Soma(num1, num2)
print(soma.interpretar())  # 15
```

### 4. **Iterator**

O padrão **Iterator** fornece uma maneira de acessar elementos de uma coleção sequencialmente, sem expor a estrutura interna da coleção. Ele separa a responsabilidade de percorrer a coleção da própria coleção.

#### Exemplo em Python:

```python
class Colecao:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, item):
        self.itens.append(item)
    
    def __iter__(self):
        return Iterador(self.itens)

class Iterador:
    def __init__(self, itens):
        self.itens = itens
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.itens):
            item = self.itens[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Testando
colecao = Colecao()
colecao.adicionar("Item 1")
colecao.adicionar("Item 2")
colecao.adicionar("Item 3")

for item in colecao:
    print(item)
```

### 5. **Mediator**

O padrão **Mediator** facilita a comunicação entre objetos, permitindo que eles se comuniquem de forma centralizada e evitando que fiquem diretamente dependentes uns dos outros.

#### Exemplo em Python:

```python
class Mediador:
    def __init__(self):
        self.componentes = []
    
    def registrar(self, componente):
        self.componentes.append(componente)
    
    def notificar(self, origem, mensagem):
        for componente in self.componentes:
            if componente != origem:
                componente.receber(mensagem)

class Componente:
    def __init__(self, nome, mediador):
        self.nome = nome
        self.mediador = mediador
        self.mediador.registrar(self)

    def enviar(self, mensagem):
        print(f"{self.nome} envia: {mensagem}")
        self.mediador.notificar(self, mensagem)

    def receber(self, mensagem):
        print(f"{self.nome} recebeu: {mensagem}")

# Testando
mediador = Mediador()

componente1 = Componente("Componente 1", mediador)
componente2 = Componente("Componente 2", mediador)

componente1.enviar("Oi, Componente 2!")
```

### 6. **Observer**

O padrão **Observer** define uma dependência de um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

#### Exemplo em Python:

```python
class Observador:
    def atualizar(self, mensagem):
        pass

class ObservadorConcretoA(Observador):
    def atualizar(self, mensagem):
        print(f"Observador A recebeu: {mensagem}")

class ObservadorConcretoB(Observador):
    def atualizar(self, mensagem):
        print(f"Observador B recebeu: {mensagem}")

class Sujeito:
    def __init__(self):
        self.observadores = []
    
    def adicionar_observador(self, observador):
        self.observadores.append(observador)
    
    def notificar_observadores(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)

# Testando
sujeito = Sujeito()
observador_a = ObservadorConcretoA()
observador_b = ObservadorConcretoB()

sujeito.adicionar_observador(observador_a)
sujeito.adicionar_observador(observador_b)

sujeito.notificar_observadores("Estado alterado!")
```

### 7. **State**

O padrão **State** permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá mudar sua classe.

#### Exemplo em Python:

```python
class Estado:
    def fazer_algo(self):
        pass

class EstadoConcretoA(Estado):
    def fazer_algo(self):
        return "Estado A está fazendo algo"

class EstadoConcretoB(Estado):
    def fazer_algo(self):
        return "Estado B está fazendo algo"

class Contexto:
    def __init__(self):
        self.estado = EstadoConcretoA()

    def alterar_estado(self, novo_estado):
        self.estado = novo_estado

    def executar(self):
        print(self.estado.fazer_algo())

# Testando
contexto = Contexto()
contexto.executar()  # Estado A está fazendo algo

contexto.alterar_estado(EstadoConcretoB())
contexto.executar()  # Estado B está fazendo algo
```

### 8. **Strategy**

O padrão **Strategy** define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. O algoritmo pode ser selecionado em tempo de execução.

#### Exemplo em Python:

```python
class Estrategia:
    def executar(self):
        pass

class EstrategiaA(Estrategia):
    def executar(self):
        return "Executando Estratégia A"

class EstrategiaB(Estrategia):
    def executar(self):
        return "Executando Estratégia B"

class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def executar_estrategia(self):
        print(self.estrategia.executar())

# Testando
contexto = Contexto(EstrategiaA())
contexto.executar_estrategia()  # Executando Estratégia A

contexto.estrategia = EstrategiaB()
contexto.executar_estrategia()  #
```


Executando Estratégia B

````

### 9. **Template Method**

O padrão **Template Method** define o esqueleto de um algoritmo em um método, deixando alguns passos para que as subclasses os implementem. Ele permite que a estrutura do algoritmo seja preservada, mas permite a personalização dos passos.

#### Exemplo em Python:

```python
class Algoritmo:
    def template_method(self):
        self.passo1()
        self.passo2()
        self.passo3()

    def passo1(self):
        pass
    
    def passo2(self):
        pass
    
    def passo3(self):
        pass

class AlgoritmoConcreto(Algoritmo):
    def passo1(self):
        print("Passo 1 do algoritmo concreto")

    def passo2(self):
        print("Passo 2 do algoritmo concreto")

    def passo3(self):
        print("Passo 3 do algoritmo concreto")

# Testando
algoritmo = AlgoritmoConcreto()
algoritmo.template_method()
````

### 10. **Visitor**

O padrão **Visitor** permite adicionar novas operações a uma estrutura de objetos sem alterar as classes dessas estruturas. O visitante "visita" os elementos e executa operações específicas para cada tipo de elemento.

#### Exemplo em Python:

```python
class Elemento:
    def aceitar(self, visitante):
        pass

class ElementoConcretoA(Elemento):
    def aceitar(self, visitante):
        visitante.visitar_elemento_a(self)

class ElementoConcretoB(Elemento):
    def aceitar(self, visitante):
        visitante.visitar_elemento_b(self)

class Visitante:
    def visitar_elemento_a(self, elemento):
        pass

    def visitar_elemento_b(self, elemento):
        pass

class VisitanteConcreto(Visitante):
    def visitar_elemento_a(self, elemento):
        print("Visitando Elemento A")

    def visitar_elemento_b(self, elemento):
        print("Visitando Elemento B")

# Testando
elemento_a = ElementoConcretoA()
elemento_b = ElementoConcretoB()

visitante = VisitanteConcreto()
elemento_a.aceitar(visitante)
elemento_b.aceitar(visitante)
```

---

### Resumo dos Padrões Comportamentais:

* **Chain of Responsibility**: Passa uma solicitação através de uma cadeia de objetos até que um deles a trate.
* **Command**: Encapsula uma solicitação como um objeto, permitindo sua execução em diferentes contextos.
* **Interpreter**: Define uma maneira de interpretar uma linguagem ou expressão.
* **Iterator**: Permite iterar sobre elementos de uma coleção sem expor sua estrutura interna.
* **Mediator**: Centraliza a comunicação entre objetos para reduzir dependências diretas.
* **Observer**: Notifica múltiplos objetos sobre mudanças em um sujeito.
* **State**: Permite que um objeto altere seu comportamento dependendo do seu estado interno.
* **Strategy**: Define uma família de algoritmos e permite que eles sejam selecionados em tempo de execução.
* **Template Method**: Define a estrutura de um algoritmo, permitindo que os detalhes sejam implementados por subclasses.
* **Visitor**: Adiciona novas operações a objetos sem modificar suas classes.


## Resumo Geral

### Design Patterns (Padrões de Projetos)

Design Patterns são soluções reutilizáveis para problemas comuns que surgem no design de software. Eles oferecem uma forma padronizada e comprovada de construir sistemas mais flexíveis, compreensíveis e robustos. São divididos em três categorias principais: Criação, Estrutura e Comportamento.

---

## Criação

Os padrões de criação lidam com a criação de objetos, abstraindo o processo de instanciação. Isso ajuda a tornar um sistema independente de como seus objetos são criados, compostos e representados.

* **Abstract Factory**: Cria famílias de objetos relacionados sem especificar suas classes concretas.

Imagina que você tem uma linha de montagem de carros e precisa produzir diferentes tipos de carros (sedãs, SUVs) e cada tipo tem diferentes componentes (motor, pneus) que devem ser compatíveis. A Abstract Factory é como ter um "super gerente de fábrica" que sabe como criar todas as peças para um tipo específico de carro (ex: peças de sedã ou peças de SUV), sem que você precise saber os detalhes de cada peça.

* **Builder**: Separa a construção de um objeto complexo da sua representação.

Pensa em construir um sanduíche. Você pode ter vários ingredientes e a ordem em que você os adiciona pode mudar o sanduíche final. O Builder é como um "chef" que recebe suas instruções (adicione pão, depois queijo, depois presunto) e monta o sanduíche para você, peça por peça, garantindo que o resultado final seja complexo, mas a sua forma de pedir é simples.

* **Factory Method**: Cria objetos em uma superclasse, mas permite que subclasses alterem o tipo de objeto.

Você é dono de uma loja de brinquedos e seus clientes querem diferentes tipos de brinquedos (carros, bonecas). O Factory Method é como ter um "balcão de fabricação" onde o cliente pede um brinquedo e, dependendo do que ele pede, a fábrica de carros ou a fábrica de bonecas é acionada para produzir o item, sem que o cliente precise saber qual fábrica específica está fazendo o trabalho.

* **Prototype**: Cria novos objetos clonando objetos existentes.

Imagine que você tem uma receita de bolo que adora e quer fazer várias cópias idênticas. Em vez de escrever a receita do zero toda vez, o Prototype é como ter um "carimbo" da receita original. Você apenas "carimba" e faz uma cópia, podendo fazer pequenas alterações se quiser, sem ter que refazer todo o trabalho.

* **Singleton**: Garante que uma classe tenha apenas uma instância.

Pense no presidente de um país. Há apenas um presidente em um determinado momento e todos os assuntos importantes passam por ele. O Singleton garante que uma classe tenha apenas uma instância e que todos acessem a mesma instância, como ter um único ponto de controle global para algo importante.

---

## Estrutura

Os padrões de estrutura descrevem como classes e objetos são compostos para formar estruturas maiores, tornando as estruturas mais flexíveis e eficientes.

* **Adapter**: Converte a interface de uma classe para outra, permitindo que interfaces incompatíveis trabalhem juntas.

Você tem um plug de tomada novo que não se encaixa na sua tomada antiga. O Adapter é como um "adaptador de tomada" que permite que o plug novo funcione na tomada antiga, convertendo a interface de um para o outro.

* **Bridge**: Desacopla a abstração da implementação, permitindo variações independentes de ambos.

Imagine que você está projetando um controle remoto (abstração) para diferentes TVs (implementação). A Bridge permite que você projete o controle remoto independentemente do tipo de TV, e você pode facilmente usar o mesmo controle para TVs de marcas diferentes. Ou seja, você não precisa criar um controle para cada marca de TV.

* **Composite**: Permite tratar objetos compostos e objetos simples de forma uniforme, formando uma estrutura hierárquica.

Pense em um organograma de uma empresa. Você pode ter um gerente (objeto composto) que tem vários funcionários (objetos simples) e outros gerentes (objetos compostos) sob sua supervisão. O Composite permite que você trate tanto um funcionário individual quanto um departamento inteiro (composto por funcionários e gerentes) da mesma forma.

* **Decorator**: Adiciona funcionalidades adicionais a um objeto sem modificar sua estrutura.

Você tem um café simples, mas quer adicionar chantilly, calda e chocolate. O Decorator é como adicionar "extras" ao seu café sem mudar o café em si. Cada extra é um decorador que adiciona uma nova funcionalidade (e talvez um custo) ao seu café original.

* **Facade**: Simplifica o uso de um subsistema complexo fornecendo uma interface única.

Pensa em um complexo sistema de som de um carro. Para tocar música, você precisaria ligar o rádio, sintonizar a estação, ajustar o volume, etc. A Facade é como um "painel de controle" simplificado que tem apenas um botão "Ligar/Desligar Música". Ele esconde toda a complexidade por trás de uma interface simples.

* **Flyweight**: Compartilha objetos comuns para economizar memória quando você tem muitas instâncias similares.

Imagine que você está criando um jogo com milhares de árvores na tela. Em vez de criar um objeto de árvore para cada uma, o Flyweight é como ter um "molde" de árvore que é compartilhado por todas as árvores iguais. Apenas as características únicas de cada árvore (sua posição, por exemplo) são armazenadas separadamente, economizando muita memória.

* **Proxy**: Fornece um substituto ou representante de outro objeto, controlando o acesso ao objeto real.

Você tem um documento confidencial em um cofre e precisa de permissão para acessá-lo. O Proxy é como um "assistente" que você pede o documento. O assistente verifica suas credenciais antes de ir até o cofre e pegar o documento real. Ele atua como um intermediário, controlando o acesso ao objeto real.

---

## Comportamento

Os padrões de comportamento lidam com a comunicação entre objetos e a atribuição de responsabilidades. Eles se concentram nos algoritmos e na forma como as interações são gerenciadas.

* **Chain of Responsibility**: Passa uma solicitação através de uma cadeia de objetos até que um deles a trate.

Pensa em uma fila de atendimento ao cliente. Se um atendente não conseguir resolver seu problema, ele passa para o próximo atendente mais especializado, e assim por diante, até que alguém resolva. A solicitação (seu problema) percorre a "cadeia de responsabilidade" até ser tratada.

* **Command**: Encapsula uma solicitação como um objeto, permitindo sua execução em diferentes contextos.

Imagina um controle remoto de TV. Cada botão (ligar, mudar canal, aumentar volume) é um "comando". O Command encapsula a ação que deve ser executada em um objeto, permitindo que você enfileire comandos, desfaça operações ou até mesmo envie comandos para serem executados por outro dispositivo.

* **Interpreter**: Define uma maneira de interpretar uma linguagem ou expressão.

Você está usando uma calculadora que entende a sintaxe "2 + 3". O Interpreter é como o "cérebro" da calculadora que entende essa linguagem específica e sabe como realizar a operação de soma.

* **Iterator**: Permite iterar sobre elementos de uma coleção sem expor sua estrutura interna

Pensa em folhear um livro. Você não precisa saber como o livro é encadernado ou quantas páginas ele tem para lê-lo página por página. O Iterator é como o "ato de folhear" que permite que você acesse os elementos de uma coleção (como as páginas de um livro) um por um, sem se preocupar com a estrutura interna da coleção.

* **Mediator**: Centraliza a comunicação entre objetos para reduzir dependências diretas.

Imagine uma torre de controle de aeroporto. Em vez de cada avião se comunicar diretamente com todos os outros aviões no espaço aéreo, a torre de controle (o mediador) coordena todas as comunicações, evitando colisões e simplificando o tráfego.

* **Observer**: Notifica múltiplos objetos sobre mudanças em um sujeito.

Você se inscreve para receber notificações de um canal de notícias. Sempre que há uma notícia nova (o estado do objeto "canal de notícias" muda), você (o observador) e todos os outros inscritos são automaticamente notificados.

* **State**: Permite que um objeto altere seu comportamento dependendo do seu estado interno.

Pensa em um semáforo. Ele pode estar no estado "vermelho", "amarelo" ou "verde". O comportamento do semáforo (o que ele faz) muda dependendo do seu estado atual. O padrão State permite que o objeto mude seu comportamento quando seu estado interno muda.

* **Strategy**: Define uma família de algoritmos e permite que eles sejam selecionados em tempo de execução.

Você está planejando uma viagem e pode escolher diferentes formas de transporte: carro, ônibus ou avião. Cada forma de transporte é uma "estratégia" para chegar ao seu destino. O padrão Strategy permite que você escolha qual estratégia usar em tempo de execução, dependendo da situação.

* **Template Method**: Define a estrutura de um algoritmo, permitindo que os detalhes sejam implementados por subclasses.

Imagina uma receita de bolo que tem passos fixos (misturar ingredientes, assar), mas alguns passos (decoração) podem ser personalizados por quem faz o bolo. O Template Method define o esqueleto do algoritmo, mas permite que subclasses implementem os detalhes específicos de certos passos.

* **Visitor**: Adiciona novas operações a objetos sem modificar suas classes.

Você tem uma coleção de figuras geométricas (círculos, quadrados, triângulos) e quer calcular a área de cada uma. Em vez de adicionar um método `calcular_area()` em cada classe de figura, o Visitor é como um "inspetor" que visita cada figura e sabe como calcular a área para cada tipo específico de figura, sem modificar as classes das figuras.




### **Portifólio**

https://tinyurl.com/5dpr33pv
