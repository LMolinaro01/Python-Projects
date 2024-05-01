import sqlite3
import tkinter
from tkinter import *
from tkinter import Tk, font
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk

# Janelas


def telaInicial():
    global telaInicio
    telaInicio = tkinter.Tk()
    telaInicio.title("Inicio")
    telaInicio.resizable(False, False)

    label = tkinter.Label(
        telaInicio, text="Bem vindo ao Sistema de Estoque!", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10, sticky='ew')

    image1 = Image.open("Projetos\Sistema de Estoque\logo.png")
    width, height = 200, 200
    image1.thumbnail((width, height))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(telaInicio, image=test)
    label1.image = test
    label1.grid(row=1, column=1, pady=10, padx=47)

    button = tkinter.Button(telaInicio, text="Adicionar ao Estoque", font="Consolas 10",
                            bg="#6B58FF", fg="white", command=telaAddProd)
    button.grid(row=2, column=1, padx=20, pady=10, sticky='ew')

    botao_prova = tkinter.Button(
        telaInicio, text="Editar Produto", font="Consolas 10", bg="#3D8EF0", fg="white", command= telaEditProd)
    botao_prova.grid(row=3, column=1, padx=20, pady=10, sticky='ew')

    botao_tabela = tkinter.Button(
        telaInicio, text="Exibir Estoque", font="Consolas 10", bg="#1CB9E4", fg="white", command=selectProd)
    botao_tabela.grid(row=4, column=1, padx=20, pady=10, sticky='ew')

    button = tkinter.Button(telaInicio, text="Sair do Programa", font="Consolas 10",
                            bg="#4A2ED1", fg="white", command=telaInicio.destroy)
    button.grid(row=5, column=1, padx=160, pady=50)

    telaInicio.mainloop()

def telaAddProd():
    global janelaAdd
    janelaAdd = tkinter.Tk()
    janelaAdd.resizable(False, False)

    janelaAdd.title("Cadastro de Produtos")

    label = tkinter.Label(
        janelaAdd, text="Preencha os campos a seguir", font="Consolas 13 bold")
    label.grid(row=0, column= 1, pady=10, sticky='ew')

    label_nome = tkinter.Label(janelaAdd, text="Nome:", font="Consolas 10")
    label_nome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janelaAdd, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=8, pady=15, sticky='ew')

    label_qtde = tkinter.Label(janelaAdd, text="Qtde:", font="Consolas 10")
    label_qtde.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textoQtde = tkinter.StringVar()
    qtde = tkinter.Entry(janelaAdd, textvariable=textoQtde)
    qtde.grid(row=2, column=1, padx=8, pady=15, sticky='ew')

    label_preco = tkinter.Label(janelaAdd, text="Preço:", font="Consolas 10")
    label_preco.grid(row=3, column=0, padx=10, pady=15, sticky='ew')
    textopreco = tkinter.StringVar()
    preco = tkinter.Entry(janelaAdd, textvariable=textopreco)
    preco.grid(row=3, column=1, padx=8, pady=15, sticky='ew')

    botao_add = tkinter.Button(janelaAdd, text="Concluir", bg="#6B58FF",
                               fg="white", command=lambda: addProd(nome.get(), qtde.get(), preco.get()))
    botao_add.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    botao_voltar = tkinter.Button(janelaAdd, text="Voltar para Tela Inicial",
                                  bg="#3D8EF0", fg="white", command=janelaAdd.destroy)
    botao_voltar.grid(row=5, column=1, padx=100, pady=10, sticky='ew')

def telaEditProd():
    rootEdit = tkinter.Tk()
    rootEdit.resizable(False, False)
    rootEdit.title("Editar Produto")
    rootEdit.geometry("622x400")

    label = tkinter.Label(
        rootEdit, text="Selecione o Produto que deseja Editar", font="Consolas 13 bold")
    label.grid(row=0, column= 0, pady=10, sticky='ew')

    cursor.execute("SELECT * FROM Produtos")
    dados = cursor.fetchall()

    tabela = tkinter.Frame(rootEdit)
    tabela.grid(row=1, column=0, padx=10, pady=10)

    tv = tkinter.ttk.Treeview(tabela, columns=(
        'nome', 'preco', 'qtde'), show='headings')
    tv.heading("nome", text='Nome')
    tv.heading('preco', text='Preço')
    tv.heading('qtde', text='Quantidade')

    for linha in dados:
        preco = linha[3]
        if preco:
            preco_formatado = 'R$ {:.2f}'.format(float(preco))
        else:
            preco_formatado = ''
        tv.insert('', 'end', values=(linha[1], preco_formatado, linha[2]))

    tv.pack()
    botao_editar = tkinter.Button(
        rootEdit, text="Editar", bg="#6B58FF", fg="white", command=rootEdit.destroy)
    botao_editar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    botao_fechar = tkinter.Button(
        rootEdit, text="Voltar", bg="#1CB9E4", fg="white", command=rootEdit.destroy)
    botao_fechar.grid(row=3, column=0, padx=100, pady=10, sticky="ew")


# Banco de Dados
connection = sqlite3.connect("Database.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Produtos (iD INTEGER PRIMARY KEY, nome TEXT, qtde INTEGER, preco REAL)")


def addProd(nome, qtde, preco):
    janelaAdd.destroy()

    try:
        qtde = int(qtde)
        preco = float(preco.replace(',', '.').replace('R$', ''))
        cursor.execute(
        "INSERT INTO Produtos (nome, qtde, preco) VALUES (?, ?, ?)", (nome, qtde, preco))
        connection.commit()
    except ValueError:
        mb.showerror(
            "Erro", "Por favor, insira uma quantidade e preço válidos.")
        return

    mb.showinfo(
        "Sucesso", f"'{nome}'({qtde}) Adicionado ao Estoque .")
    
    if mb.askyesno("Adicionar outro produto", "Deseja adicionar outro produto?"):
        telaAddProd()


def selectProd():
    rootEdit = tkinter.Tk()
    rootEdit.resizable(False, False)
    rootEdit.title("Tabela de Produtos")
    rootEdit.geometry("622x400")

    cursor.execute("SELECT * FROM Produtos")
    dados = cursor.fetchall()

    tabela = tkinter.Frame(rootEdit)
    tabela.grid(row=0, column=0, padx=10, pady=10)

    tv = tkinter.ttk.Treeview(tabela, columns=(
        'nome', 'preco', 'qtde'), show='headings')
    tv.heading("nome", text='Nome')
    tv.heading('preco', text='Preço')
    tv.heading('qtde', text='Quantidade')

    for linha in dados:
        preco = linha[3]
        if preco:
            preco_formatado = 'R$ {:.2f}'.format(float(preco))
        else:
            preco_formatado = ''
        tv.insert('', 'end', values=(linha[1], preco_formatado, linha[2]))

    tv.pack()
    botao_fechar = tkinter.Button(
        rootEdit, text="Voltar", bg="#6B58FF", fg="white", command=rootEdit.destroy)
    botao_fechar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


telaInicial()

addProd("Samsung A12", 12, 789.90)
addProd("Samsung A12", 8, 899.90)
addProd("Samsung Galaxy S21", 12, 3451.00)
addProd("Samsung Galaxy S23", 12,  2969.10)
addProd("Mangá 'GoGo Monster'", 8,  85.50)
addProd("Mangá 'Os Gatos do Louvre Vol. 01'", 12,  61.43)
connection.commit()
