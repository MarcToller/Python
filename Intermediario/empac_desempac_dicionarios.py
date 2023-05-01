# Empacotamento e desempacotamento de dicionários

pessoa2 = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa2 # neste caso, a vai receber o nome da promeira chave "nome" e b o nome da segunda chave "sobrenome"
a, b = pessoa2.values() # assim vai retrnar a = Aline e b = Sousa
a, b = pessoa2.items() # retorna 2 tuplas: a = (nome = Aline) e b = (Sobrenome = Sousa)
(a1, a2), b = pessoa2.items() # a1 = nome, a2 = Aline, b = (Sobrenome = Sousa)



pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# Unindo dois dicionários!
pessoas_completa = {**pessoa, **dados_pessoa} 
pessoas_completa = {**pessoa, **dados_pessoa, 'chave': 1} # poderia passar mais chaves e valores se quisesse
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados) - 2 asteríscos!

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(1,2,3, nome='Joana', idade=20) # 1, 2 e 3 são os args e os outros são são o kwargs
mostro_argumentos_nomeados(**configuracoes) # passando somente kwargs (ele entende que os args esta vazio e não dá erro )
mostro_argumentos_nomeados(1,2, **configuracoes) # 1 e 2 são os args e **configurações são o kwargs