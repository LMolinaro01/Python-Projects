import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

def mover_arquivos(pasta_origem):
    contador = 1

    for raiz, diretorios, arquivos in os.walk(pasta_origem, topdown=False):
        for arquivo in sorted(arquivos): 
            caminho_arquivo = os.path.join(raiz, arquivo)
            
            extensao = os.path.splitext(arquivo)[1]  
            novo_nome = f"file_{contador}{extensao}"  
            destino = os.path.join(pasta_origem, novo_nome)

            # Verifica se o arquivo já não está na pasta principal
            if os.path.exists(destino):
                print(f"O arquivo {novo_nome} já existe na pasta principal. Ignorando.")
            else:
                # Move o arquivo para a pasta principal e renomeia
                shutil.move(caminho_arquivo, destino)
                print(f"Movido e renomeado: {caminho_arquivo} para {destino}")
                contador += 1
        
        # Remove a subpasta depois de mover seus arquivos
        if raiz != pasta_origem:
            try:
                os.rmdir(raiz)
                print(f"Removida a subpasta: {raiz}")
            except OSError:
                print(f"Não foi possível remover a subpasta {raiz}, talvez ela não esteja vazia.")

def selecionar_pasta():
    Tk().withdraw()  # Esconde a janela principal
    pasta = askdirectory(title="Selecione uma pasta")  # Solicita ao usuário selecionar uma pasta
    return pasta

def main():
    pasta_origem = selecionar_pasta()  # Seleciona a pasta pelo usuário
    
    if pasta_origem:
        print(f"Você escolheu a pasta: {pasta_origem}")
        mover_arquivos(pasta_origem)
    else:
        print("Nenhuma pasta selecionada. O programa será encerrado.")

if __name__ == "__main__":
    main()