#definindo a classe

from random import (randint)

class dado (object):# aqui fiz a classe dado
    """simula um dado"""
    def __init__(self,lados):   #informações que o objeto necessita
        """param lados = quantidade de lados do seu dado"""
        self.lado = lados
    def roll (self,mod=0):      # depois  os métodos que podem ser aplicados no objeto dado
        """ rola o seu dado virtual,
            ou seja entrega um valor aleatório entre 1 e o numero de lados dele
            e depois adiciona o mod(modificador) ao resultado final e retorna esse valor"""
        x = randint(1,self.lado)
        x = x+mod
        return(x)
    def rollv (self,mod=0):
        """rola o dado 2 vezes,e retorna o valor da maior rolagem
        somada do param mod(modificador)"""
        roll1 = randint(1,self.lado)
        roll2 = randint(1,self.lado)
        maior = roll1
        if roll2 > roll1:
            maior = roll2
        maior += mod
        return (maior)
    def rolld(self,mod=0):
        """rola o dado 2 vezes,e retorna o valor da menor rolagem
         somada do param mod(modificador)"""
        roll1 = randint(1, self.lado)
        roll2 = randint(1, self.lado)
        menor = roll1
        if roll2 < roll1:
            menor = roll2
        menor += mod
        return (menor)







