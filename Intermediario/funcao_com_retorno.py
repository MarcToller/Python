"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y # o return funciona igual ao JS: Qdo é chamado ele não executa mais nada abaixo.


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))