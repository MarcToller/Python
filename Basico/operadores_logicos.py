
############ OPERADOR AND (Igual no Delphi)

# usuario = input('Digite o usuário: ')
# senha = input('Digite a senha: ')
# if (usuario == 'toller') and (senha == '123456'): # não precisa dos parenteses, que que quis colocar
#     print('acesso concedido')
# else:
#     print('acesso negado') 
# Zero (0) ,  Zero ponto zero (0.0) e  string vazia ('') retornam elas mesmas e não false, isso se chama falsy ex.:
# print(True and True and 0.0 and True) # retona 0.0
  
############# OPERADOR OR
# usuario = input('Digite o usuário: ')
# senha = input('Digite a senha: ')
# if ((usuario == 'toller') or (usuario == 'TOLLER')) and (senha == '123456'): # NO CASO DO OR PRECISA DE PARENTES, NÃO POR DAR ERRO, MAS POR LÓGICA MESMO
#     print('acesso concedido')
# else:
#     print('acesso negado')
# TEM UM RECURSO IGUAL NO JAVASCRIPT:
# senha = input('Digite a senha') or 'Senha não digitada' # aqui se não digitar nada retorna a string 'Senha não digitada'
# print(senha)

############# OPERADOR NOT 
# senha = input('Digite a senha: ')
# if not senha:
#     print('Você não digitou nada') 
# else:    
#     print(senha)

############# OPERADOR IN E NOT IN
# String iteráveis, indices positivos e negativos:
# 0 1 2 3 4 5
# T o l l e r
#-6-5-4-3-2-1 # quando o indice é negativo, começa no -1 pois o 0 é foi considerado no inicio positivo  
nome = 'Toller'
print(nome[2]) # vai mostrar l
print(nome[-2]) # vai mostrar e
print('r' in nome) # true
print('ler' in nome) # true
print('tr' in nome) # false
print('z' not in nome) # true

nome = input('digite o nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

        


