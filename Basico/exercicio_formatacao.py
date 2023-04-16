
nome = input('Digite seu nome: ')
idade = input('Digite sua iade: ')

if not nome and not idade:
    print('Você não digitou nenhuma informação.')
elif not nome:
    print('Você não digitou o nome.')
elif not idade:
    print('Você não digitou a idade')
else:
    print(f'Seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    # Esse find ele não ensinou, descobri aqui mas pode usar um in
    #if nome.find(' ', 0) > -1:
    if ' ' in nome:
        print(f'seu nome possui espaço')
    else:    
        print(f'seu nome não possui espaço')

    print(f'Seu nome possui {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    
    #print(f'A última letra do seu nome é {nome[len(nome)-1]}') dá p usar o indice -1
    print(f'A última letra do seu nome é {nome[-1]}')



