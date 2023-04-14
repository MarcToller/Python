
"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
############## LEMBRANDO QUE O PYTHON É CASE SENSITIVE!!!
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a' # TRUE
igual = 'a' == 'A' # FALSE
diferente = 'a' != 'b'
#print(diferente)

# EXERCICIO
vValor1 = input('Digite o valor 1: ')
vValor2 = input('Digite o valor 2: ')

vValorint1 = int(vValor1)
vValorint2 = int(vValor2)

if vValorint1 > vValorint2:
    print(f'{vValorint1=} é maior que {vValorint2=}')
elif vValorint1 < vValorint2:
    print(f'{vValorint2=} é maior que {vValorint1=}')
else:  
    print(f'{vValorint1=} é igual ao {vValorint2=}')
      

