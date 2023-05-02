# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor # Map com Condição ternária, vai pegar a chave e o valor maiusculo somente se o valor for do tipo str. Posso perguntar por mais de um tipo assim: isinstance(valor, (str, float))
    for chave, valor in produto.items() # aqui é o for no dicionário
    if chave != 'categoria' # filter
}


# posso criar um novo dicionário a partir de uma lista com tuplas que sejam similares a "chave" e "valor" que tenham essa "dupla"
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

# Assim tab daria:
# print(dict(lista))


s1 = {2 ** i for i in range(10)} # criando um set que coloca o numero 2 fixo elevado a cada item de 0 a 10, só que não fica na ordem
print(s1)