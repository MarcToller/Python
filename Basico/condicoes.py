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
