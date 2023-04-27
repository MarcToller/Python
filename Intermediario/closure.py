"""
Closure e funções que retornam outras funções
"""


# esta função retorna a sub função para ser executada lá fora!
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia') # aqui a variavel falar_bom_dia já fica "preparada" para quando for chamada ela já "guardou" esse bom dia para ser usado agora quantas vezes precisar!
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

############## exercício #################

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
multiplica_por_2 = criar_multiplicador(2)    
multiplica_por_3 = criar_multiplicador(3)

print(multiplica_por_2(10))
print(multiplica_por_3(10))
      

