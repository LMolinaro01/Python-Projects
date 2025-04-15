df_teste["a"].apply(lambda x: x+1)
df_teste["a"].apply(to_Dolar(y)) #realiza um tratamento de dados, usando uma função 

#o que é printado é apenas uma tabela temporária, não irá salvar por cima do dataframe original

#para salvar por cima

df_teste["c"] = df_teste.apply(lambda x: x["a"] + x["b"]) #a coluna "c" será a soma das colunas "a" e "b"

df_teste["c"] = df_teste.apply(lambda x: regex_limpeza(x)) # limpar dados sensíveis (cpf, endereço completo)