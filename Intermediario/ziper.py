# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
from itertools import zip_longest
import os

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
#print(list(zip(l1, l2)))
#print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))

a = [{'nome': 'aaaa', 'idade': 40},
     {'nome': 'aaaa', 'idade': 30}]

b = [{'nome': 'paulo', 'idade': 4},
     {'nome': 'maria', 'idade': 3}]

c = [{'nome': 'www', 'idade': 9},
     {'nome': 'yyy', 'idade': 7}]

Lista = (list(zip(a, b, c)))

#for tupla in Lista:
#    for dicionario in tupla:
#        print(dicionario['nome'], dicionario['idade'])

for tupla in Lista:
    for dic in tupla:
     print(dic)
    

