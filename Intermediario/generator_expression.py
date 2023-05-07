import sys

# Generator expression, Iterables e Iterators em Python
lista = [n for n in range(1000000)] # A lista já é criada e salva na memória
generator = (n for n in range(1000000)) # o generator não

print(sys.getsizeof(lista)) # Tamanho em memória da list
print(sys.getsizeof(generator)) # Tamanho em memória do generator

# generator não tem indice e nem tamanho (len) só sabe quem é o próximo valor
print(generator)

# for n in generator:
#     print(n)


################ GENERATION FUNCTION ################

def generator():
    yield 1 # esse yield pausa a cada chamadada função
    print('Continuando..')
    yield 2
    print('Mais uma..')    
    yield 3
    print('Vou terminar..')    
    return 'Acabou' # esse return tem a função de retornar esse texto somente em caso de a função ser chamada e já tenha acabado as iterações, como se fosse uma descrição para o execpt

gen = generator()
print(next(gen)) # vai imprimir 1
print(next(gen)) # vai imprimir "Continuando.." e 2
print(next(gen)) # vai "Mais uma.." e 3
print(next(gen)) # vai imprimir "Vou terminar.." mas vai cair na exceção "return Acabou" pois tem 3 pausas (yield) mas 4 chamadas

# A forma correta:
for n in gen:
    print(n)


# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)


# Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()    