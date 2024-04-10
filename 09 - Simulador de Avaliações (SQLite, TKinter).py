#EM ANDAMENTO

import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk

connection = sqlite3.connect("Database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (nome TEXT, senha TEXT, curso TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS Questoes (enunciado TEXT, resposta TEXT, ID TEXT)")

#root = None

def telaInicial():
    global root
    root = tkinter.Tk()
    root.title("Página Inicial")
    root.resizable(False, False)
    root.geometry("300x500")

    image1 = Image.open("logoEstacio.png")
    width, height = 200, 200
    image1.thumbnail((width, height))

    # criei uma instância do objeto ImageTk para exibir a imagem no tkinter
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(root, image=test)
    label1.image = test
    label1.grid(row=1, column=1, pady=10, padx = 47)

    label = tkinter.Label(root, text="Bem vindo ao Simulado")
    label.grid(row=0, column=1, pady=10)

    button = tkinter.Button(root, text="Cadastre-se", bg="#009FD6", fg="white", command = abrirJanelaAluno)
    button.grid(row=2, column=1, pady=10)

    botao_prova = tkinter.Button(root, text="Realizar Prova", bg="#009FD6", fg="white", command=validarJanelaProva)
    botao_prova.grid(row=3, column=1, padx=10, pady=10)

    button = tkinter.Button(root, text="Sair do Programa", bg="#009FD6", fg="white", command = lambda : root.destroy())
    button.grid(row=4, column=1, pady=10)

    root.mainloop()
        

def abrirJanelaAluno():
    global root
    root.withdraw() #fecha janela inicial
    janelaAluno()

def janelaAluno():
    global root
    root.withdraw()

    janela2 = tkinter.Tk()
    janela2.geometry("270x400")
    janela2.title("Cadastro Aluno")

    #nome
    label_nome = tkinter.Label(janela2, text="Nome:")
    label_nome.grid(row=0, column=0, padx=10, pady=15)
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janela2, textvariable=textoNome)
    nome.grid(row=0, column=1, padx=10, pady=15)
    
    #senha
    label_senha = tkinter.Label(janela2, text="Senha:")
    label_senha.grid(row=1, column=0, padx=10, pady=15)
    textosenha = tkinter.StringVar()
    senha = tkinter.Entry(janela2, textvariable=textosenha)
    senha.grid(row=1, column=1, padx=10, pady=15)
    
    #curso
    label_curso = tkinter.Label(janela2, text="Curso:")
    label_curso.grid(row=2, column=0, padx=10, pady=10)
    textocurso = tkinter.StringVar()
    curso = tkinter.Entry(janela2, textvariable=textocurso)
    curso.grid(row=2, column=1, padx=10, pady=10)
    
    botao_cadastrar = tkinter.Button(janela2, text="Cadastre-se", bg="#009FD6", fg="white", command=lambda: verificarCadastroAluno(nome.get(), senha.get(), curso.get()))
    botao_cadastrar.grid(row=3, column=1, padx=10, pady=10)
    
def adicionarAluno(nome, senha, curso):
    caracteres_especiais = ";-'!,+:."
    if any(caracter in caracteres_especiais for caracter in str(nome) + str(senha) + str(curso)):
        print("Caracteres especiais não são permitidos.")
    else:
        cursor.execute("INSERT INTO Alunos (nome, senha, curso) VALUES (?, ?, ?)", (nome, senha, curso))
        connection.commit()

def verificarLogin(nome, senha):
    query = "SELECT * FROM Alunos WHERE nome=? AND senha=?"
    cursor.execute(query, (nome, senha))
    aluno = cursor.fetchone()
    
    caracteres_especiais = ";-'!+."
    if any(caracter in caracteres_especiais for caracter in str(nome) + str(senha)):
        mb.showinfo("Aviso", "Caracteres especiais não são permitidos.")
        
    elif not(nome and senha):       
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")

    elif aluno:
        janelaProva()
    else:
        mb.showinfo("Aviso", "Credenciais inválidas.")

def verificarCadastroAluno(nome, senha, curso):
    caracteres_especiais = ";-'!+."
    if any(caracter in caracteres_especiais for caracter in str(nome) + str(senha) + str(curso)):
        mb.showinfo("Aviso", "Caracteres especiais não são permitidos.")
        
    elif not(nome and senha and curso): #verifica se está vazio        
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")
        
    else:
        mb.showinfo("Sucesso", "Cadastro válido.")
        adicionarAluno(nome, senha, curso)
        validarJanelaProva()

def validarJanelaProva():
    global root
    root.withdraw()

    global janelaValidProva
    janelaValidProva = tkinter.Tk()
    janelaValidProva.geometry("270x400")
    janelaValidProva.title("Faça seu Login como Aluno")

    #nome
    label_nome = tkinter.Label(janelaValidProva, text="Nome:")
    label_nome.grid(row=0, column=0, padx=10, pady=15)
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janelaValidProva, textvariable=textoNome)
    nome.grid(row=0, column=1, padx=10, pady=15)
    
    #senha
    label_senha = tkinter.Label(janelaValidProva, text="Senha:")
    label_senha.grid(row=1, column=0, padx=10, pady=15)
    textosenha = tkinter.StringVar()
    senha = tkinter.Entry(janelaValidProva, textvariable=textosenha)
    senha.grid(row=1, column=1, padx=10, pady=15)
    
    botao_cadastrar = tkinter.Button(janelaValidProva, text="Realize seu Login", bg="#009FD6", fg="white",command=lambda: verificarLogin(nome.get(), senha.get()))
    botao_cadastrar.grid(row=3, column=1, padx=10, pady=10)

def janelaProva():
    global janelaValidProva
    janelaValidProva.withdraw()

    global janelaProva
    janelaProva = tkinter.Toplevel()
    janelaProva.title("Prova da Estácio")
    #janelaProva.geometry("900x800")
    janelaProva.resizable(True, False)

    e = str(cursor.execute("SELECT enunciado from Questoes where ID = 1").fetchall())
    print(e)
    connection.commit()

    v = tkinter.IntVar()
    v2 = tkinter.IntVar()
    v3 = tkinter.IntVar()
    v4 = tkinter.IntVar()

    #Questão 1 
    label = tkinter.Label(janelaProva, text="Questão 1) Escolha o resultado da seguinte operação: Integral de 2x")
    label.grid(row=1, column=0, padx=10, pady=10)

    tkinter.Radiobutton(janelaProva, text="x²/2", variable=v, value=1).grid(row=2, column=0, sticky="w", padx=10, pady=5) #sticky w alinha com da esquerda
    tkinter.Radiobutton(janelaProva, text="2x²", variable=v, value=2).grid(row=3, column=0, sticky="w", padx=10, pady=5)
    tkinter.Radiobutton(janelaProva, text="x²/2 + c", variable=v, value=3).grid(row=4, column=0, sticky="w", padx=10, pady=5) #correta
    tkinter.Radiobutton(janelaProva, text="x² + c", variable=v, value=4).grid(row=5, column=0, sticky="w", padx=10, pady=5)
    
    #Questão 2
    label2 = tkinter.Label(janelaProva, text="Questão 2) Calcule a derivada da seguinte função: f(x) = 2x+1")
    label2.grid(row=7, column=0, padx=10, pady=10)

    tkinter.Radiobutton(janelaProva, text="f(x)' = 2x", variable=v2, value=1).grid(row=8, column=0, sticky="w", padx=10, pady=5)
    tkinter.Radiobutton(janelaProva, text="f(x)' = x + 1", variable=v2, value=2).grid(row=9, column=0, sticky="w", padx=10, pady=5)
    tkinter.Radiobutton(janelaProva, text="f(x)' = 2", variable=v2, value=3).grid(row=10, column=0, sticky="w", padx=10, pady=5) #correta
    tkinter.Radiobutton(janelaProva, text="f(x)' = x/2", variable=v2, value=4).grid(row=11, column=0, sticky="w", padx=10, pady=5)
    
    #Questão 3 
    label3 = tkinter.Label(janelaProva, text="Questão 3) A área de um triângulo que possui 12 cm de altura e base medindo 9 cm é:")
    label3.grid(row=13, column=0, padx=10, pady=10)

    tkinter.Radiobutton(janelaProva, text="54 cm²", variable=v3, value=1).grid(row=14, column=0, sticky="w", padx=10, pady=5) #correta
    tkinter.Radiobutton(janelaProva, text="70 cm²", variable=v3, value=2).grid(row=15, column=0, sticky="w", padx=10, pady=5)
    tkinter.Radiobutton(janelaProva, text="85 cm²", variable=v3, value=3).grid(row=16, column=0, sticky="w", padx=10, pady=5)
    tkinter.Radiobutton(janelaProva, text="108 cm²", variable=v3, value=4).grid(row=17, column=0, sticky="w", padx=10, pady=5)

    botao_finalizar = tkinter.Button(janelaProva, text="Concluir Prova", bg="#009FD6", fg="white",command=lambda: verificarFimProva())
    botao_finalizar.grid(row=17, column=1, padx=10, pady=10)

def verificarFimProva():
    resposta = mb.askyesno("Finalizar Prova", "Deseja realmente finalizar a prova?")
    if resposta:
        finalizarProva()

def finalizarProva():
    global janelaProva
    janelaProva.withdraw()

    janelaResultProva = tkinter.Toplevel()
    janelaResultProva.title("Resultado da Prova")
    janelaResultProva.geometry("300x400")
    janelaResultProva.resizable(False, False)

    label = tkinter.Label(janelaResultProva, text="Nome: ")
    label.grid(row=0, column=0, padx=10, pady=10)

    label = tkinter.Label(janelaResultProva, text="Curso: ")
    label.grid(row=1, column=0, padx=10, pady=10)

    label = tkinter.Label(janelaResultProva, text="Pontuação Final: ")
    label.grid(row=2, column=0, padx=10, pady=10)

    botao_Resposta = tkinter.Button(janelaResultProva, text="Resolução das Questões", bg="#009FD6", fg="white",command=lambda: ResolucaoProva())
    botao_Resposta.grid(row=3, column=0, padx=10, pady=10)

def ResolucaoProva():
    janelaRespProva = tkinter.Toplevel()
    janelaRespProva.title("Gabarito")
    #janelaRespProva.geometry("480x425")
    janelaRespProva.resizable(False, False)

    #Questão 1 
    label = tkinter.Label(janelaRespProva, text="Questão 1) Escolha o resultado da seguinte operação: Integral de 2x")
    label.grid(row=0, column=0, padx=10, pady=10)

    labelR = tkinter.Label(janelaRespProva, text="Resposta: 2x²/2 + c = x² + c")
    labelR.grid(row=1, column=0, padx=10, pady=10)
    
    #Questão 2
    label2 = tkinter.Label(janelaRespProva, text="Questão 2) Calcule a derivada da seguinte função: f(x) = 2x+1")
    label2.grid(row=2, column=0, padx=10, pady=10)

    label2R = tkinter.Label(janelaRespProva, text="Resposta: 2.")
    label2R.grid(row=3, column=0, padx=10, pady=10)
    
    #Questão 3 
    label3 = tkinter.Label(janelaRespProva, text="Questão 3) A área de um triângulo que possui 12 cm de altura e base medindo 9 cm é:")
    label3.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    label3R = tkinter.Label(janelaRespProva, text="Resposta: b.h/2 = 9*12/2 = 54 cm²")
    label3R.grid(row=5, column=0, padx=10, pady=10)


telaInicial()

'''e = str(cursor.execute("SELECT * from Alunos").fetchall())
print(e)
connection.commit()'''
