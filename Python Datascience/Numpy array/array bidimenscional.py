import numpy as np

my_array = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
print(my_array.shape) # imprime quantidade de (linhas,colunas)do array

a = np.arange(6).reshape((3, 2)) # mudando forma do array
print(a)
my_array[0][0]= -1 # modificando elemento do array
print(my_array)

# array vazia
x = np.empty([3,2], dtype = int)
print(x)
#array valores aleatórios
my_random_array = np.random.random((5))
print(my_random_array)
#array valores aleatórios num range escolhido
a = np.floor(10*np.random.random((3,4)))
print(a)
# fatiando array - fatia igual lista
# cada linha sendo como uma lista dentro da lista
