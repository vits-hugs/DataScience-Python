import  matplotlib.pyplot as plt
year = [1950,1970,1990]
pop = [2.519,3.692,5.263]
# adicionando dados
pop = [1,1.262,1.650] + pop
year =[1800,1850,1900] + year
plt.plot(year,pop) # grafico linha
plt.scatter(year,pop) #grafico bolinhas
# decorando
plt.xlabel('ano')
plt.ylabel('população em bilhões')
plt.title('Projeção da população mundial')
# dividindo o grafico por numero e dando palavras
plt.yticks([0,2,4,6,8,10],
        ['0','2B','4B','6B','8B','10B'])
# colorindo
plt.fill_between(year,pop,0,color='green')

plt.show()