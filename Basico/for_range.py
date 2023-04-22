"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8) # vai do 0 a 100 de 8 em 8

lista = ['a', 'b', 'c']
numeros = range(len(lista)) # vai de 0 a 2 pois são os índices da lista

for numero in numeros:
    print(numero)