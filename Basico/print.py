# Print pode ser executado com vários argumentos, seja numero ou string.
# se eu passar 2 argumentos por exemplo ele vai imprimir com espaço entre eles
# para colocar um separador diferente de espaço utilizamos o argumento nomeado sep:
# pode-se usar aspas simples ou duplas

print(1,2,3,4, sep='-')

# argumento nomeado "end", por padrão ele já é uma quebra de linha, mas poemos mudar:

print(5, 6, 7, 8, sep='-', end='\r\n') # o \r\n já é o quebra linha, então aqui nada muda, dependendo do windows só o \n jáfunciona
print(9, 10, 11, 12, sep='-', end='##\n')
print(9, 10, 11, 12, sep='-', end='\nteste')

