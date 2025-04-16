import csv
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def converter_csv_para_json():
    # Janela oculta principal
    janela = tk.Tk()
    janela.withdraw()

    # Selecionar arquivo CSV
    caminho_csv = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv")]
    )

    if not caminho_csv:
        messagebox.showwarning("Aviso", "Nenhum arquivo CSV foi selecionado.")
        return

    # Selecionar onde salvar o JSON
    caminho_json = filedialog.asksaveasfilename(
        title="Salvar como JSON",
        defaultextension=".json",
        filetypes=[("Arquivos JSON", "*.json")]
    )

    if not caminho_json:
        messagebox.showwarning("Aviso", "Caminho para salvar o JSON não foi definido.")
        return

    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            dados = list(leitor)

        with open(caminho_json, mode='w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)

        messagebox.showinfo("Sucesso", f"Conversão concluída!\nJSON salvo em:\n{caminho_json}")
    except Exception as erro:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{erro}")

# Chamada principal
if __name__ == "__main__":
    converter_csv_para_json()
