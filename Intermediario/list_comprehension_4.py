

# FOR DENTRO DE FOR NA LIST comprehension

# mais sobre o assunto:
# https://www.youtube.com/watch?v=1YbTDczvqco

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)