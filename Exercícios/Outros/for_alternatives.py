from functools import reduce

#Funções alternativas ao For

    #Sum - Soma os dados de um array

array1 = [0,1,2,3,4,5]
print(sum(array1))

    #Filter - Realiza uma Filtragem

def maior_que_10(x):
    return x >10

array2 = [7,8,9,10,11,12,13] #função filtro | Array
num_filtrados = list(filter(maior_que_10, array2))
print(num_filtrados)

    #Map - transformação em cada item

def triplicar(x):
    return x * 3

mapped_items = []
for item in [1,2,3]:
    mapped_items.append(triplicar(item))

print(mapped_items)

#Melhor solução:

mapped_items2 = list(map(triplicar, [1,2,3]))
print(mapped_items2)

    #Reduce - reduz todos os valores para apenas um 
    # (aplica a função subsequentemente, um item atrás do outro)

def add(x, y):
    return x + y

num = [1,2,3,4,5]

total_sum = reduce(add, num) #soma como se o array fosse uma expressão numérica (de soma)
print(total_sum)

#pega o resultado da primeira soma e faz com a segunda    


