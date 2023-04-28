p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome') Apaga a chave e retorna o valor
# print(nome)
# print(p1)
# ultima_chave = p1.popitem() # este apaga sempre o último item e devolve um dicionario com a chave e o valor excluído
# print(ultima_chave)
# print(p1)

# update altera o valor de uma chave já existente ou adiciona uma nova chave
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

# p1.update(nome='novo valor', idade=30) pode ser feito direto assim tb

# tupla = (('nome', 'novo valor'), ('idade', 30)) ou assim enviando um iteravel em "duplas" que seria a chave e valor
# p1.update(tupla)

#lista = [['nome', 'novo valor'], ['idade', 30]]
#p1.update(lista)
print(p1)