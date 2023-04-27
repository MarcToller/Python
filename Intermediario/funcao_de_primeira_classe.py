"""
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.

"""


# Basicamente uma funcao que chama outra função que é passada por parametro

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)  # aqui aconteceu um desempacotamente de *args e passou os 2 parametros para a função Saudacao


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)

# Posso tb jogar uma função para uma variável e "executar" a variável

def teste(argumento):
    return argumento*10

variavel = teste

print(variavel(10))

