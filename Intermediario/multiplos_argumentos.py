"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args): # esse args é uma convensão, mas pode-se colocar qualqur nome!                   
    total = 0    # os múltiplos parametros passados nesse *args é uma tupla que pode ser convertida em lista ou pode ser iterada. Esses argumentos são Não nomeados! Importante isso para mais lá na frente!
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) # aqui se pssar uma tupla no parametro, como o parametro é *args que já é uma tupla, ficaria uma tupla dentro da outra, então se tiver que passar uma tupla ou lista neste parametro, fazemos o desempacotamento da lista com *
print(outra_soma)

print(sum(numeros))
# print(*numeros)

#################### EXERCÍCIOS ####################

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplicar(3,3,3)
print(resultado) 


def par_ou_impar(numero):
    return 'Par' if numero % 2 == 0 else 'Ímpar'

print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(25145582))
