#vários pdf em 1 só

import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import os

def merge_pdfs(pdf_files, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    print(f"PDFs mesclados com sucesso! O arquivo de saída é: {output_path}")

# Abrir a interface para selecionar os PDFs
Tk().withdraw()  # Esconde a janela principal do Tkinter
pdf_files = askopenfilenames(title="Selecione os PDFs", filetypes=[("PDF files", "*.pdf")])

if pdf_files:
    output_path = os.path.join(os.getcwd(), "output_merged.pdf")
    merge_pdfs(pdf_files, output_path)
else:
    print("Nenhum arquivo PDF foi selecionado.")