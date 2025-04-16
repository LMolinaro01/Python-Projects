import pandas as pd #apelido

meus_dados = pd.read_csv("abc.csv")
meus_dados2 = pd.read_excel("abc.xcsx")
meus_dados3 = pd.read_json("abc.json")

meus_dados = pd.read_csv(R"C:\\Arquivos de Programas\Dados\abc.csv") #o r serve para o python não confundir a \
meus_dados = pd.read_csv(r"C://Arquivos de Programas/Dados/abc.csv") #linux e mac

