"""


Tipo tupla - Uma lista imutável

"""

nomes = 'Maria', 'Helena', 'Luiz'
# ou
nomes = ('Maria', 'Helena', 'Luiz')
# ou
nomes = tuple(nomes)
# ou
nomes = list(nomes)

print(nomes[-1])
print(nomes)

# converter lista para tupla:
lista = ['a', 'b', 'c']
tupla = tuple(lista)

# converter tupla para lista:
tupla = ('a', 'b', 'c')
lista = list(tupla)