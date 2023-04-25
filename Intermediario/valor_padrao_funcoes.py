"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z=None):
    # Definição
    # esse none é como se fosse o nil, só que em python, se eu colocar 0 como defaul e depois perguntar por ele, vai dar um False pois 0 retorna false
    if z is not None: # se eu tivesse colocado 0 no defaul e perguntado por "if z:" isso retornaria um false
        print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)



soma(1, 2, 0)
soma(1, y=2, z=5)
soma(1, 2)