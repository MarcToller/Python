

# copy - retorna uma cópia rasa (shallow copy) só copia dados imutáveis do dicionário, se dentro do dicionário tiver uma lista, ela não ai copiar mas vai referenciar ele na cópia, ou seja, se alterar a lista num dicionário vai alterar no outro copiado tb

# deepcopy - precisa importar o modulo copy e usar a função deepcopy, aí sim ele copya tudo, todos os níveis do dicionario

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy() # não vai copiar a l1, só vai referenciar ela no d2
d2 = copy.deepcopy(d1) # vai copiar tudo de di para d2

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)