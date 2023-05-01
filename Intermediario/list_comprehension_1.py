# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero * 2 for numero in range(10)] # dá para fazer um for dentro da lista e com condicionamentos! O que vai alimentar a lista é o que tem à esquerda do form neste caso numero * 2
print(lista)