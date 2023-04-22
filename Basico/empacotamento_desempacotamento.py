"""

Introdução ao empacotamento e desempacotamento

PELO QUE ENTENDI É SEMELHANTE AO RECURSO DO JS MAS LÁ É CHAMADO DE DESASSOCIAÇÃO EU ACHO..

"""
nomes = ['Marcelo', 'Ana', 'Paula']
nome1, nome2, nome3 = nomes
# as variáveis vão receber os respectivos valores na ordem da lista
print(nome1)

# Pegar apenas o primeiro valor: uSo uma variável de "resto" aonde ele vai empacotar o restante da lista, usa-se o asterísco:
nome1, *resto = nomes
print(nome1, resto)

# Quando quisermos dizer que existe uma variável que não vaamos usar ou nãao vai ser nessesária, existe uma convensão que se cria uma váriável com underline, sim, ela é só um _
# então se eu quiser só o 3 nome por exemplo:
_, _, nome = ['Maria', 'Helena', 'Luiz']
print(nome)