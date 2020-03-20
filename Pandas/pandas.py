import pandas as pd
#Aprendendo a usar funcionalidades de pandas
# trazendo arquivo brics.csv
bric = pd.read_csv("brics.csv",index_col = 0)
#print(bric)
# agora você pode se referir a uma coluna assim:
bric['país']
#ou assim
bric.país
# pode fazer uma coluna nova
bric['naterra'] = ['sim','sim','sim','sim','sim']

# e pode calcular com as colunas,e colocar o conteudo numa nova coluna
bric['densidade'] = bric['população']/bric['área']*1000000
print(bric)
#acessando linhas
print(bric.loc['BR'])
#acessando um termo especifico
bric['capital'].loc['BR']#assim
bric.loc['BR']['capital']#ou assim
bric.loc['BR','capital']#ou assim
