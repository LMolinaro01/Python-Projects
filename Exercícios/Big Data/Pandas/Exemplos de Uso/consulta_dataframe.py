df_teste = pd.dataframe([{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 0, "b": 5},{"a": 10, "c": 50}])

df_teste["a"] #exibe a coluna A
df_teste.loc[2] #exibe a linha 2 (numerada pelo pandas)
df_teste.iloc[2] #exibe a linha de posição 2 

df_teste.loc([T,F,F,T]) #exibe a primeira e a quinta linha 
df_teste.loc([df_teste["a"]>2]) #exibe as linhas maiores que a 2 da coluna A (retorna um verdadeiro ou falso também)
