"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(z=1, x=2, y=3) # quando nomeados podemos chamar em qualquer ordem
soma(1, y=2, z=5) # posso começar a nomear a partir de um deles..
# soma(1, y=2, 5) mas a partir do momento que eu nomeio um parametro, todos que vierem após tem que ser nomeados tb

