# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista, Modo):
    for item in lista:
        print('Modo'+Modo, item)
    print()

# Modo 1
# defino uma função que retorna a chave que vai ser usada o ordenar:
def ordenar(item):
    return item['nome']

lista.sort(key=ordenar)
exibir(lista, '1')

# Modo 2: alterar a própria lista: com um "método anônimo" pelo que entendi, função lambda são os métodos anônimos no Delphi
lista.sort(key=lambda item: item['nome'])
exibir(lista, '2')

# Modo 3: com um "método anônimo" pelo que entendi, função lambda são os métodos anônimos no Delphi
# porém criando uma nova lista com uma cópia raza:
l1 = sorted(lista, key=lambda item: item['nome']) # a palabra lambda aqui seria o def de uma função, o item seria o parametro mas não recebe parenteses, o que vem depois dos 2 pontos seria o return

l2 = sorted(lista, key=lambda item: item['sobrenome'])
exibir(l1, '3')
exibir(l2, '3')