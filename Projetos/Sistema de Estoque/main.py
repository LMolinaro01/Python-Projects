import random
import sqlite3
import tkinter
from tkinter import *
from tkinter import Tk, font
from tkinter import messagebox as mb
from PIL import Image, ImageTk

def telaInicial():
    global telaInicio
    telaInicio = tkinter.Tk()
    telaInicio.title("Inicio")
    telaInicio.resizable(False, False)

    label = tkinter.Label(telaInicio, text="Bem vindo ao Sistema de Estoque!", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10, sticky='ew')

    image1 = Image.open("Projetos\Sistema de Estoque\logo.png")
    width, height = 200, 200
    image1.thumbnail((width, height))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(telaInicio, image=test)
    label1.image = test
    label1.grid(row=1, column=1, pady=10, padx=47)

    button = tkinter.Button(telaInicio, text="Adicionar ao Estoque", font= "Consolas 10", 
                            bg="#6B58FF", fg="white")
    button.grid(row=2, column=1, padx=20, pady=10, sticky='ew')

    botao_prova = tkinter.Button(
        telaInicio, text="Editar Produto", font= "Consolas 10", bg="#3D8EF0", fg="white")
    botao_prova.grid(row=3, column=1, padx=20, pady=10, sticky='ew')

    botao_tabela = tkinter.Button(
        telaInicio, text="Exibir Estoque", font= "Consolas 10", bg="#1CB9E4", fg="white")
    botao_tabela.grid(row=4, column=1, padx=20, pady=10, sticky='ew')

    button = tkinter.Button(telaInicio, text="Sair do Programa", font= "Consolas 10",
                            bg="#4A2ED1", fg="white", command=lambda: telaInicio.destroy())
    button.grid(row=5, column=1, padx=120, pady=50)

    telaInicio.mainloop()

telaInicial()