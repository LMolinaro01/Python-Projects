import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
 
def janela():
    root = tkinter.Tk()
    root.title("Janela do SIA")
    root.resizable(True, True)
    label = tkinter.Label(root, text="Estácio")
    label.pack()
    label = tkinter.Label(root, text="SIA - Sistema de Informações Acadêmicas")
    label.pack()
    botaoAzul = tkinter.Button(root, text="Entrar com e-mail de estudante")
    botaoAzul.pack()
 
    label = tkinter.Label(root, text="------------- ou -------------")
    label.pack()
 
    label = tkinter.Label(root, text="Matricula")
    label.pack()
    textomatricula = tkinter.StringVar()
 
    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.pack()
 
    label = tkinter.Label(root, text="Senha")
    label.pack()
    textosenha = tkinter.StringVar()
 
    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.pack()
 
    label2 = tkinter.Label(root, textvariable=textoEntrada)
    label2.pack()
 
    botao = tkinter.Button(root, text="Entrar")
    botao.pack()
 
janela()
