pode_entrar = input('pode entrar? ')

# O BEGIN/END SÃO AS IDENTAÇÕES
if pode_entrar == 'S':
    print('sim') 
    print('Você pode entrar')
elif pode_entrar == 'N':
    print('Não')
    print('Você não pode entrar')
else:
    print('digite S ou N')       

# para quebrar uma condição em outra linha podemos usar a barra invertida :
a = 0;
b = 1

if (a + b == 0) and \
     (b == 0) and \
        (a > 0):    
    print('bla bla')