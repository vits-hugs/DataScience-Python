import numpy as np
np_city= np.array([[4,10,3],[9,4,2],[10,4,5]])
print(np.mean(np_city[:,0])) # média
print(np.median(np_city[:,0])) # mediana
# numpy tem seu sum() e sort() são mais rapido pq usam mesmo tipo
# primeiro valor é média,segundo não
altura = np.round(np.random.normal(1.75,0.20, 500),3)
peso = np.round(np.random.normal(60.32,15, 500),3)
np_tudo = np.column_stack((altura,peso))
print(np.median(np_tudo[:,0]))
