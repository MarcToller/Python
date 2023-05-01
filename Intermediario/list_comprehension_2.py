

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# tem um código dentro de uma lista!! muito louco isso!
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # as chaves indicam que eu criei um dicionario vazio, e desempacotei o dicionario que esta sendo prcorrido (**produto) dentro deste novo dicionário e setando a chave 'preço' para ela mesma mais um percentual de aréscimo, como a chave já existe, ele apenas altera o seu valor! Muito louco isso
    if produto['preco'] > 20 else {**produto} # aqui temos uma condição ternária, ou seja, vai executa aquela parte ali de cima se o preço for maior que 20, senão apenas desempacota o próprio dicionário dentro de um novo (else {**produto})

    for produto in produtos # percorrendo a lista de dicionarios e acima fazendo um aumento de preço condicional
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')
