import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import imageio_ffmpeg as ffmpeg

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Selecione o arquivo MKV",
        filetypes=[("Arquivos MKV", "*.mkv")]
    )

def listar_legendas(mkv_path):
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    comando = [ffmpeg_path, "-i", mkv_path]
    resultado = subprocess.run(comando, stderr=subprocess.PIPE, text=True)
    linhas = resultado.stderr.splitlines()

    faixas = []
    for linha in linhas:
        if "Subtitle" in linha:
            faixas.append(linha.strip())
    return faixas

def extrair_legenda(mkv_path, faixa_index, output_path):
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    comando = [
        ffmpeg_path, "-i", mkv_path,
        "-map", f"0:s:{faixa_index}",
        output_path
    ]
    subprocess.run(comando)

def main():
    mkv_path = selecionar_arquivo()
    if not mkv_path:
        print("Nenhum arquivo selecionado.")
        return

    print("🔍 Procurando faixas de legenda...")
    faixas = listar_legendas(mkv_path)

    if not faixas:
        print("Nenhuma legenda encontrada.")
        return

    print("\nLegendas encontradas:")
    for i, faixa in enumerate(faixas):
        print(f"[{i}] {faixa}")

    escolha = int(input("\nEscolha o número da legenda que deseja extrair: "))
    nome_base = os.path.splitext(os.path.basename(mkv_path))[0]
    output_path = os.path.join(
        os.path.dirname(mkv_path),
        f"{nome_base}_legenda_{escolha}.srt"
    )

    extrair_legenda(mkv_path, escolha, output_path)
    print(f"\n✅ Legenda salva em: {output_path}")

if __name__ == "__main__":
    main()