# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

import pprint # pretty print, ou seja, um print bonito


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    ]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} # mapeamento com if ternário, é como se fosse um complemento do filter
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # este if é o filtro, só vai cair no mapeamento acima do for (e estar sujeito a alteracao ou não no if ternário) caso a condição do filtro seja atendida
]
p(novos_produtos)

# Exemplo mais simples:
lista = [n for n in range(10)  if n < 5] # esse if n < é o filtro
p(lista)