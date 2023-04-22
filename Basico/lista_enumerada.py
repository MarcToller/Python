"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']

Lista_enumerada = enumerate(lista)

# for item_enumerado in Lista_enumerada:
#     print(item_enumerado) # aqui ele gera uma tupla coom 2 valores: o indice e o valor em si
# # se repetir aqui em baixo, não vai acontecer nada pois ele itera e elimina a lista!!!!    
# for item_enumerado in Lista_enumerada:
#     print(item_enumerado) 
# Mas se fizer assim não ocorre essa situação:
# for item_enumerado in enumerate(lista)
#     print(item_enumerado) 


for indice, nome in enumerate(lista): # parecido com o que tem em JS
    print(indice, nome, lista[indice])

for item in enumerate(lista, start=19): # posso definir um start, mas esse start é para começar por exemplo no 19, ou seja, o item 0 assume 19, ele não vai começar a partir do 19, mas sim transformar o 0 em 19, o 1 em 20 e assim ´por diante    
    indice, nome = item # parecido com o que tem em JS
    print(indice, nome)

# posso converter um enumerate para lista
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
Lista_enumerada = list(enumerate(lista))     
print(Lista_enumerada) # mostra uma lista de listas, cada item da lista tem uma "lista" de 2 itens: indice e valor


for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}') # o \t da um tab
