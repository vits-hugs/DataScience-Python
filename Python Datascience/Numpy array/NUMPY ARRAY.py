import numpy as np
# explicação https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355
# Aqui eu transformo as listas em numpy arrays
height = [1.73,1.68,1.71]
weight = [65.4,59.2,63.6]
np_height = np.array(height)
np_weight = np.array(weight)
#é outro tipo embutido no python
#assim como lista é diferente de tupla,array são diferentes
# e vão ter interações diferentes com mesmo código

# aqui vemos a funcionalidade de calculo
# com essa expressão
# ele pega cada weight e calcula com sua especifica height
bm = np_weight/np_height**2

bm >21 # True ou False pra cada elemento,se > 21 = True se não False
print(bm[bm >21] ) # só pega os elementos maiores de 21
