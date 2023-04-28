# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
   # 'idade': 900,
}

pessoa.setdefault('idade', 0) # caso não tenha a chave retorna o valor defaul, se tiver então pega o valor da chave, mas ele acaba adicionando essa chave se não existir! Já o get não adiciona
print(pessoa['idade'])
print(pessoa) # para mostrar como o setdefault adicionou a chave

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items())) Posso converter para lista com list()

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)