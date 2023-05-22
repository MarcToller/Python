
# aqui eu tenho acesso a 3 escopos! 

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


# Posso usar quantos decoradores eu quiser, aqui ele vai executar os decoradores de baixo para cima, nest caso ele concatna o parametro nome no resultado
@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)



# Outro exemplo

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) # aqui, além de passar os parametros 1,2,3 ele ainda passa a função soma para o segundo escopo!
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores() # aqui ele passa o primeiro escopo, mas como os parametros são default então não precisou passa nada
multiplica = decoradora(lambda x, y: x * y) # aqui  ele já passou os parametros do primeiro escopo (a,b,c) acima e agora esta passando uma função, neste caso uma lambda que é um método anônimo

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
