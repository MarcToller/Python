"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz') # adiciona no final
nome = lista.pop() # excluí o último e ainda retorna o valor excluío, mas eu posso passar o ínice que quero excluir
lista.append(1233)
del lista[-1] # apaga o último item da lista
# lista.clear() Limpa tods os valores da lista          
lista.insert(100, 5) # insere no um valor em determinado indice, o oposto do pop. neste caso, se não existir o indie 100 ele não vai gerar erro, vai simplesmente adicionar na última posição.
print(lista[4])

# ordenar listas
lista3 = [2,39,8,41,12,54,56]
lista3.sort() # altera a propria lista
lista3.sort(reverse=True) # inverte a ordenação

# assim ordena e cria uma nova lista
lista4 = sorted(lista3, reverse=True)
print(lista3)
print(lista4)


#  extend - estende a lista
#  + - concatena listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b) ERRADO!!!
lista_a.extend(lista_b) #CERTO!!
print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # tudo que eu fizer em uma vai refletir na outra, os dois apontam p mesmo endereço.
lista_b = lista_a.copy() # assim não ocorre o problema acima.

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))