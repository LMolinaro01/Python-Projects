import psycopg2
from psycopg2 import sql
import tkinter as tk
from tkinter import ttk, messagebox as mb
from time import strftime
import datetime
from PIL import Image, ImageTk

# ========================
# Configurações do Banco
# ========================
DB_HOST = "insira aqui"
DB_NAME = "insira aqui"
DB_USER = "insira aqui"
DB_PASSWORD = "insira aqui"

# ========================
# Modelo (Model)
# ========================
class Database:
    def connect(self):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conn
        except Exception as e:
            print(f"Erro na conexão com o banco: {e}")
            return None

    def create_tables(self):
        conn = self.connect()
        if conn is None:
            return
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS Produtos (
                            iD SERIAL PRIMARY KEY,
                            nome TEXT,
                            qtde INTEGER,
                            preco REAL
                        )
                    """)
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS Vendas (
                            iD SERIAL PRIMARY KEY,
                            nomeVenda TEXT,
                            qtde INTEGER,
                            precoTotal REAL,
                            data TEXT
                        )
                    """)
                    print("Tabelas criadas/verificadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")
        finally:
            conn.close()

    def get_baixo_estoque_count(self, threshold=5):
        conn = self.connect()
        if conn is None:
            return 0
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT COUNT(*) FROM Produtos WHERE qtde < %s", (threshold,))
                    count = cur.fetchone()[0]
            return count
        except Exception as e:
            print(f"Erro ao contar estoque baixo: {e}")
            return 0
        finally:
            conn.close()

    def get_produtos(self):
        conn = self.connect()
        if conn is None:
            return []
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM Produtos")
                    rows = cur.fetchall()
            return rows
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
            return []
        finally:
            conn.close()

    def insert_produto(self, nome, qtde, preco):
        conn = self.connect()
        if conn is None:
            return
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO Produtos (nome, qtde, preco) VALUES (%s, %s, %s)", (nome, qtde, preco))
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
        finally:
            conn.close()

    def update_produto(self, id_produto, nome, qtde, preco):
        conn = self.connect()
        if conn is None:
            return
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE Produtos SET nome=%s, qtde=%s, preco=%s WHERE iD=%s", (nome, qtde, preco, id_produto))
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
        finally:
            conn.close()

    def delete_produto(self, id_produto):
        conn = self.connect()
        if conn is None:
            return
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM Produtos WHERE iD=%s", (id_produto,))
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
        finally:
            conn.close()

    def update_produto_quantidade(self, id_produto, qtde_vendida):
        conn = self.connect()
        if conn is None:
            return
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE Produtos SET qtde = qtde - %s WHERE iD = %s", (qtde_vendida, id_produto))
        except Exception as e:
            print(f"Erro ao atualizar quantidade: {e}")
        finally:
            conn.close()

    def get_produto_by_id(self, id_produto):
        conn = self.connect()
        if conn is None:
            return None
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM Produtos WHERE iD = %s", (id_produto,))
                    row = cur.fetchone()
            return row
        except Exception as e:
            print(f"Erro ao buscar produto por ID: {e}")
            return None
        finally:
            conn.close()

    def insert_venda(self, nomeVenda, qtde, precoTotal, data):
        conn = self.connect()
        if conn is None:
            return
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO Vendas (nomeVenda, qtde, precoTotal, data) VALUES (%s, %s, %s, %s)", 
                        (nomeVenda, qtde, precoTotal, data)
                    )
        except Exception as e:
            print(f"Erro ao inserir venda: {e}")
        finally:
            conn.close()

    def get_vendas(self):
        conn = self.connect()
        if conn is None:
            return []
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM Vendas")
                    rows = cur.fetchall()
            return rows
        except Exception as e:
            print(f"Erro ao buscar vendas: {e}")
            return []
        finally:
            conn.close()

# Instancia do Model e criação das tabelas
db = Database()
db.create_tables()

# ========================
# Visão (View) e Controlador (Controller)
# ========================
def centralizar_janela(janela):
    janela.update_idletasks()
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posicao_x = (largura_tela // 2) - (largura_janela // 2)
    posicao_y = (altura_tela // 2) - (altura_janela // 2)
    janela.geometry(f"+{posicao_x}+{posicao_y}")

def telaInicial():
    global telaInicio
    telaInicio = tk.Tk()
    telaInicio.title("Inicio")
    telaInicio.resizable(False, False)
    telaInicio.focus_force()

    # Imagens (confira os caminhos)
    bg = tk.PhotoImage(file="Projetos/Sistema de Estoque/wallpaper.png")
    label_bg = tk.Label(telaInicio, image=bg)
    label_bg.image = bg
    label_bg.place(x=0, y=0)

    label = tk.Label(telaInicio, text="Bem vindo ao Sistema de Estoque!", font="Consolas 13 bold", bg="#FFFFFF")
    label.grid(row=0, column=1, pady=10, sticky='ew')

    image1 = Image.open("Projetos/Sistema de Estoque/logo.png")
    image1.thumbnail((400, 300))
    test = ImageTk.PhotoImage(image1)
    label_logo = tk.Label(telaInicio, image=test)
    label_logo.image = test
    label_logo.grid(row=1, column=1, pady=10, padx=47)

    button_vender = tk.Button(telaInicio, text="Área de Vendas", font="Consolas 10", bg="#6B58FF", fg="white", command=telaFinanceiro)
    button_vender.grid(row=2, column=1, padx=20, pady=10, sticky='ew')

    button_add = tk.Button(telaInicio, text="Adicionar Novo Produto", font="Consolas 10", bg="#3D8EF0", fg="white", command=telaAddProd)
    button_add.grid(row=3, column=1, padx=20, pady=10, sticky='ew')

    button_edit = tk.Button(telaInicio, text="Editar Produtos", font="Consolas 10", bg="#1CB9E4", fg="white", command=telaEditProd)
    button_edit.grid(row=4, column=1, padx=20, pady=10, sticky='ew')

    baixa_estoque_count = db.get_baixo_estoque_count(5)
    if baixa_estoque_count > 0:
        botao_tabela = tk.Button(telaInicio, text="Exibir Estoque ⚠️", font="Consolas 10 bold", bg="#0AB4B5", fg="#75163F", command=selectProd)
    else:
        botao_tabela = tk.Button(telaInicio, text="Exibir Estoque", font="Consolas 10", bg="#0AB4B5", fg="white", command=selectProd)
    botao_tabela.grid(row=5, column=1, padx=20, pady=10, sticky='ew')

    button_sair = tk.Button(telaInicio, text="Sair do Programa", font="Consolas 10", bg="#4A2ED1", fg="white", command=telaInicio.destroy)
    button_sair.grid(row=6, column=1, padx=170, pady=50)

    label_hora = tk.Label(telaInicio, font="Consolas 10", bg="#FFFFFF")
    label_hora.grid(row=7, column=1, padx=10, sticky='e')

    def atualizar_hora():
        label_hora.config(text=strftime("%H:%M:%S"))
        telaInicio.after(1000, atualizar_hora)
    atualizar_hora()

    telaInicio.mainloop()

def telaFinanceiro():
    telaInicio.withdraw()
    global janelaVendas
    janelaVendas = tk.Toplevel()
    janelaVendas.resizable(False, False)
    janelaVendas.geometry("325x520")
    janelaVendas.title("Área de Vendas")

    label = tk.Label(janelaVendas, text="Área Financeira", font="Consolas 13 bold")
    label.grid(row=0, column=0, pady=10, sticky='ew')

    imagem = Image.open("Projetos/Sistema de Estoque/logo2.png")
    imagem.thumbnail((400, 300))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(janelaVendas, image=imagem)
    label_imagem.image = imagem
    label_imagem.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    botao_vender = tk.Button(janelaVendas, text="Realizar uma Venda", bg="#6B58FF", fg="white", command=telaVenderProd)
    botao_vender.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

    botao_consulta = tk.Button(janelaVendas, text="Consultar Vendas", bg="#3D8EF0", fg="white", command=exibirVendas)
    botao_consulta.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

    botao_voltar = tk.Button(janelaVendas, text="Voltar para Tela Inicial", bg="#1CB9E4", fg="white", command=lambda: [janelaVendas.destroy(), telaInicio.deiconify()])
    botao_voltar.grid(row=4, column=0, padx=100, pady=10, sticky='ew')

def telaVenderProd():
    janelaVendas.withdraw()
    rootVender = tk.Tk()
    rootVender.resizable(False, False)
    rootVender.title("Vender Produto")
    rootVender.geometry("445x440")

    label = tk.Label(rootVender, text="Selecione o Produto que deseja Vender", font="Consolas 13 bold")
    label.grid(row=0, column=0, pady=10, sticky='ew')

    produtos = db.get_produtos()
    tabela = tk.Frame(rootVender)
    tabela.grid(row=1, column=0, padx=10, pady=10)
    tv = ttk.Treeview(tabela, columns=('id', 'nome', 'preco', 'qtde'), show='headings')
    tv.heading("id", text='ID')
    tv.column("id", width=50)
    tv.heading("nome", text='Nome')
    tv.heading('preco', text='Preço')
    tv.column("preco", width=120)
    tv.heading('qtde', text='Qtde')
    tv.column("qtde", width=50)

    for linha in produtos:
        preco = linha[3]
        preco_formatado = f'R$ {float(preco):.2f}' if preco else ''
        if linha[2] <= 5:
            tv.insert('', 'end', values=(linha[0], linha[1], preco_formatado, linha[2]), tags=("baixo_estoque",))
        else:
            tv.insert('', 'end', values=(linha[0], linha[1], preco_formatado, linha[2]))
    tv.tag_configure("baixo_estoque", foreground="#EB3324")
    tv.pack()

    def venderProduto():
        item_selecionado = tv.selection()
        if item_selecionado:
            item = tv.item(item_selecionado)
            id_produto = item['values'][0]
            produto = db.get_produto_by_id(id_produto)
            if produto:
                vender_janela = tk.Toplevel()
                vender_janela.title("Vender Produto")
                vender_janela.resizable(False, False)
                vender_janela.geometry("400x300")

                label = tk.Label(vender_janela, text="Preencha os campos a seguir", font="Consolas 13 bold")
                label.grid(row=0, column=1, pady=10, sticky='ew')

                label_nome = tk.Label(vender_janela, text="Nome:", font="Consolas 10")
                label_nome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
                textoNome = tk.StringVar(value=produto[1])
                nome = tk.Entry(vender_janela, textvariable=textoNome)
                nome.grid(row=1, column=1, padx=8, pady=15, sticky='ew')

                label_qtde = tk.Label(vender_janela, text="Qtde:", font="Consolas 10")
                label_qtde.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
                textoQtde = tk.StringVar(value="1")
                qtde = tk.Entry(vender_janela, textvariable=textoQtde)
                qtde.grid(row=2, column=1, padx=8, pady=15, sticky='ew')

                def calcular_preco_total():
                    try:
                        nova_qtde = int(qtde.get())
                        total = float(produto[3]) * nova_qtde
                        preco_total.config(text=f"R$ {total:.2f}")
                    except ValueError:
                        preco_total.config(text="R$ 0.00")

                def aumentar_quantidade():
                    try:
                        nova_quantidade = int(textoQtde.get()) + 1
                        textoQtde.set(str(nova_quantidade))
                        calcular_preco_total()
                    except ValueError:
                        pass

                botao_aumentar = tk.Button(vender_janela, text="+", bg="#6B58FF", fg="white", command=aumentar_quantidade)
                botao_aumentar.grid(row=2, column=2, padx=5, pady=15, sticky='w')

                label_preco_total = tk.Label(vender_janela, text="Preço Total:", font="Consolas 10")
                label_preco_total.grid(row=3, column=0, padx=10, pady=15, sticky='ew')
                preco_total = tk.Label(vender_janela, text="", font="Consolas 10 bold")
                preco_total.grid(row=3, column=1, padx=8, pady=15, sticky='ew')
                calcular_preco_total()

                def salvar_venda():
                    try:
                        nova_qtde = int(qtde.get())
                    except ValueError:
                        mb.showerror("Erro", "Quantidade inválida.")
                        return

                    data_atual = datetime.datetime.now()
                    data_formatada = data_atual.strftime('%H:%M:%S, %d-%m-%Y')
                    if nova_qtde <= produto[2]:
                        calcular_preco_total()
                        if mb.askyesno("Vender Produto", f"Deseja vender o Produto '{produto[1]}' por '{preco_total.cget('text')}'?"):
                            db.update_produto_quantidade(id_produto, nova_qtde)
                            db.insert_venda(produto[1], nova_qtde, preco_total.cget("text"), data_formatada)
                            mb.showinfo("Sucesso", f"Venda realizada com sucesso! Preço total: {preco_total.cget('text')}")
                            vender_janela.destroy()
                            rootVender.destroy()
                            telaInicio.destroy()
                            telaInicial()
                    else:
                        mb.showerror("Erro", "Quantidade insuficiente em estoque.")

                botao_salvar = tk.Button(vender_janela, text="Salvar", bg="#6B58FF", fg="white", command=salvar_venda)
                botao_salvar.grid(row=4, column=1, padx=5, pady=10, sticky='ew')

                botao_voltar = tk.Button(vender_janela, text="Voltar", bg="#3D8EF0", fg="white", command=vender_janela.destroy)
                botao_voltar.grid(row=5, column=1, padx=20, pady=10, sticky='ew')

    botao_vender = tk.Button(rootVender, text="Vender Produto", bg="#6B58FF", fg="white", command=venderProduto)
    botao_vender.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    botao_voltar = tk.Button(rootVender, text="Voltar", bg="#3D8EF0", fg="white", command=lambda: [rootVender.destroy(), janelaVendas.deiconify()])
    botao_voltar.grid(row=3, column=0, padx=20, pady=10, sticky='ew')

def exibirVendas():
    rootConsulta = tk.Tk()
    rootConsulta.resizable(False, False)
    rootConsulta.title("Vendas")
    rootConsulta.geometry("562x400")

    label = tk.Label(rootConsulta, text="Histórico de Vendas", font="Consolas 13 bold")
    label.grid(row=0, column=0, pady=10, sticky='ew')

    vendas_data = db.get_vendas()
    tabela = tk.Frame(rootConsulta)
    tabela.grid(row=1, column=0, padx=10, pady=10)
    tv = ttk.Treeview(tabela, columns=('ID', 'Nome', 'Quantidade', 'Preço Total', 'Data'), show='headings')
    tv.heading("ID", text='ID')
    tv.column("ID", width=50)
    tv.heading('Nome', text='Nome do Produto')
    tv.heading('Quantidade', text='Qtde')
    tv.column("Quantidade", width=50)
    tv.heading('Preço Total', text='Preço Total')
    tv.column("Preço Total", width=120)
    tv.heading('Data', text='Data')
    tv.column("Data", width=120)

    for venda in vendas_data:
        tv.insert('', 'end', values=venda)
    tv.pack()
    botao_fechar = tk.Button(rootConsulta, text="Voltar", bg="#6B58FF", fg="white", command=rootConsulta.destroy)
    botao_fechar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

def telaAddProd():
    global janelaAdd
    janelaAdd = tk.Tk()
    janelaAdd.resizable(False, False)
    janelaAdd.geometry("435x320")
    janelaAdd.title("Cadastro de Produtos")
    centralizar_janela(janelaAdd)

    label = tk.Label(janelaAdd, text="Preencha os campos a seguir", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10, sticky='ew')

    label_nome = tk.Label(janelaAdd, text="Nome:", font="Consolas 10")
    label_nome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tk.StringVar()
    nome = tk.Entry(janelaAdd, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=8, pady=15, sticky='ew')

    label_qtde = tk.Label(janelaAdd, text="Qtde:", font="Consolas 10")
    label_qtde.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textoQtde = tk.StringVar()
    qtde = tk.Entry(janelaAdd, textvariable=textoQtde)
    qtde.grid(row=2, column=1, padx=8, pady=15, sticky='ew')

    label_preco = tk.Label(janelaAdd, text="Preço:", font="Consolas 10")
    label_preco.grid(row=3, column=0, padx=10, pady=15, sticky='ew')
    textopreco = tk.StringVar()
    preco = tk.Entry(janelaAdd, textvariable=textopreco)
    preco.grid(row=3, column=1, padx=8, pady=15, sticky='ew')

    def addProd():
        janelaAdd.destroy()
        try:
            qtde_val = int(qtde.get())
            preco_val = float(preco.get().replace(',', '.').replace('R$', ''))
            db.insert_produto(nome.get(), qtde_val, preco_val)
        except ValueError:
            mb.showerror("Erro", "Por favor, insira uma quantidade e preço válidos.")
            telaAddProd()
            return
        mb.showinfo("Sucesso", f"'{nome.get()}' ({qtde.get()}) adicionado ao estoque.")
        if mb.askyesno("Adicionar outro produto", "Deseja adicionar outro produto?"):
            telaAddProd()
    botao_add = tk.Button(janelaAdd, text="Concluir", bg="#6B58FF", fg="white", command=addProd)
    botao_add.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    botao_voltar = tk.Button(janelaAdd, text="Voltar para Tela Inicial", bg="#3D8EF0", fg="white", command=lambda: [janelaAdd.destroy(), telaInicio.destroy(), telaInicial()])
    botao_voltar.grid(row=5, column=1, padx=100, pady=10, sticky='ew')

def telaEditProd():
    rootEdit = tk.Tk()
    rootEdit.resizable(False, False)
    rootEdit.title("Editar Produto")
    rootEdit.geometry("445x440")

    label = tk.Label(rootEdit, text="Selecione o Produto que deseja Editar", font="Consolas 13 bold")
    label.grid(row=0, column=0, pady=10, sticky='ew')

    produtos = db.get_produtos()
    tabela = tk.Frame(rootEdit)
    tabela.grid(row=1, column=0, padx=10, pady=10)
    tv = ttk.Treeview(tabela, columns=('id', 'nome', 'preco', 'qtde'), show='headings')
    tv.heading("id", text='ID')
    tv.column("id", width=50)
    tv.heading("nome", text='Nome')
    tv.heading('preco', text='Preço')
    tv.column("preco", width=120)
    tv.heading('qtde', text='Qtde')
    tv.column("qtde", width=50)

    for linha in produtos:
        preco = linha[3]
        preco_formatado = f'R$ {float(preco):.2f}' if preco else ''
        if linha[2] <= 5:
            tv.insert('', 'end', values=(linha[0], linha[1], preco_formatado, linha[2]), tags=("baixo_estoque",))
        else:
            tv.insert('', 'end', values=(linha[0], linha[1], preco_formatado, linha[2]))
    tv.tag_configure("baixo_estoque", foreground="#EB3324")
    tv.pack()

    def editarProduto():
        item_selecionado = tv.selection()
        if item_selecionado:
            item = tv.item(item_selecionado)
            id_produto = item['values'][0]
            produto = db.get_produto_by_id(id_produto)
            if produto:
                editar_janela = tk.Tk()
                editar_janela.title("Editar Produto")
                editar_janela.resizable(False, False)
                editar_janela.geometry("360x300")
                centralizar_janela(editar_janela)

                label = tk.Label(editar_janela, text="Preencha os campos a seguir", font="Consolas 13 bold")
                label.grid(row=0, column=1, pady=10, sticky='ew')

                label_nome = tk.Label(editar_janela, text="Nome:", font="Consolas 10")
                label_nome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
                textoNome = tk.StringVar(value=produto[1])
                nome = tk.Entry(editar_janela, textvariable=textoNome)
                nome.grid(row=1, column=1, padx=8, pady=15, sticky='ew')

                label_qtde = tk.Label(editar_janela, text="Qtde:", font="Consolas 10")
                label_qtde.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
                textoQtde = tk.StringVar(value=produto[2])
                qtde = tk.Entry(editar_janela, textvariable=textoQtde)
                qtde.grid(row=2, column=1, padx=8, pady=15, sticky='ew')

                label_preco = tk.Label(editar_janela, text="Preço:", font="Consolas 10")
                label_preco.grid(row=3, column=0, padx=10, pady=15, sticky='ew')
                textoPreco = tk.StringVar(value=produto[3])
                preco = tk.Entry(editar_janela, textvariable=textoPreco)
                preco.grid(row=3, column=1, padx=8, pady=15, sticky='ew')

                def salvar_edicao():
                    novo_nome = nome.get()
                    try:
                        nova_qtde = int(qtde.get())
                        novo_preco = float(preco.get().replace(',', '.').replace('R$', ''))
                        db.update_produto(id_produto, novo_nome, nova_qtde, novo_preco)
                        mb.showinfo("Sucesso", "Produto atualizado com sucesso!")
                        editar_janela.destroy()
                        rootEdit.destroy()
                        telaInicio.destroy()
                        telaInicial()
                    except ValueError:
                        mb.showerror("Erro", "Por favor, insira uma quantidade e preço válidos.")

                botao_salvar = tk.Button(editar_janela, text="Salvar", bg="#6B58FF", fg="white", command=salvar_edicao)
                botao_salvar.grid(row=4, column=1, padx=5, pady=10, sticky='ew')

                botao_voltar = tk.Button(editar_janela, text="Voltar", bg="#3D8EF0", fg="white", command=editar_janela.destroy)
                botao_voltar.grid(row=5, column=1, padx=20, pady=10, sticky='ew')

    def deletarProd():
        itens_selecionados = tv.selection()
        if itens_selecionados:
            itens_para_deletar = []
            for item_selecionado in itens_selecionados:
                item = tv.item(item_selecionado)
                nome_produto = item['values'][1]
                itens_para_deletar.append((item['values'][0], nome_produto))
            if mb.askyesno("Deletar Produtos", "Deseja mesmo deletar os produtos selecionados?", icon='warning'):
                for id_produto, _ in itens_para_deletar:
                    db.delete_produto(id_produto)
                rootEdit.destroy()
                telaInicio.destroy()
                telaInicial()

    botao_editar = tk.Button(rootEdit, text="Editar", bg="#6B58FF", fg="white", command=editarProduto)
    botao_editar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    botao_deletar = tk.Button(rootEdit, text="Deletar", bg="#3D8EF0", fg="white", command=deletarProd)
    botao_deletar.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
    botao_fechar = tk.Button(rootEdit, text="Voltar", bg="#1CB9E4", fg="white", command=rootEdit.destroy)
    botao_fechar.grid(row=4, column=0, padx=50, pady=10, sticky='ew')

def selectProd():
    rootSelect = tk.Tk()
    rootSelect.resizable(False, False)
    rootSelect.title("Tabela de Produtos")
    rootSelect.geometry("622x400")

    label = tk.Label(rootSelect, text="Estoque dos Produtos", font="Consolas 13 bold")
    label.grid(row=0, column=0, pady=10, sticky='ew')

    produtos = db.get_produtos()
    tabela = tk.Frame(rootSelect)
    tabela.grid(row=1, column=0, padx=10, pady=10)
    tv = ttk.Treeview(tabela, columns=('nome', 'preco', 'qtde'), show='headings')
    tv.heading("nome", text='Nome')
    tv.heading('preco', text='Preço')
    tv.heading('qtde', text='Quantidade')

    for linha in produtos:
        preco = linha[3]
        preco_formatado = f'R$ {float(preco):.2f}' if preco else ''
        if linha[2] < 10:
            tv.insert('', 'end', values=(linha[1], preco_formatado, linha[2]), tags=("baixo_estoque",))
        else:
            tv.insert('', 'end', values=(linha[1], preco_formatado, linha[2]))
    tv.tag_configure("baixo_estoque", foreground="#EB3324")
    tv.pack()
    botao_fechar = tk.Button(rootSelect, text="Voltar", bg="#6B58FF", fg="white", command=rootSelect.destroy)
    botao_fechar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Inicia a aplicação
telaInicial()
