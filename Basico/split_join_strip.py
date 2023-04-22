"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) # Strip é o mesmo que trim, o lsplit tira espaços à esquerda e o rstrip á direita

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases) # a vírgula é o separador, posso usar quelquer caractere de separação ou deixar vazio para nenhum
print(frases_unidas)