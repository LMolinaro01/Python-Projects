import random
import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk

def telaInicial():
    global telaInicio
    telaInicio = tkinter.Tk()
    telaInicio.title("Página Inicial")
    telaInicio.resizable(False, False)
    telaInicio.geometry("300x500")

    label = tkinter.Label(telaInicio, text="Bem vindo ao Sistema de Estoque!")
    label.grid(row=0, column=1, pady=10)

    image1 = Image.open("image.png")
    width, height = 200, 200
    image1.thumbnail((width, height))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(telaInicio, image=test)
    label1.image = test
    label1.grid(row=1, column=1, pady=10, padx=47)

    button = tkinter.Button(telaInicio, text="",
                            bg="#009FD6", fg="white")
    # sticky='ew' -> estica o botao horizontalmente
    button.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    botao_prova = tkinter.Button(
        telaInicio, text="", bg="#009FD6", fg="white")
    botao_prova.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    botao_tabela = tkinter.Button(
        telaInicio, text="", bg="#009FD6", fg="white")
    botao_tabela.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    button = tkinter.Button(telaInicio, text="Sair do Programa",
                            bg="#009FD6", fg="white", command=lambda: telaInicio.destroy())
    button.grid(row=5, column=1, padx=10, pady=10,
                sticky='e')  # stiky e vai pra direita

    telaInicio.mainloop()

