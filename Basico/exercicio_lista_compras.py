"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:    
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').upper()
    os.system('cls')

    if opcao == 's'.upper():
        break
    elif opcao == 'l'.upper():
        if len(lista_compras) == 0:
            print('Nenhum item na lista')
        else:    
            for indice, produto in enumerate(lista_compras):
                print(indice, produto)
    elif opcao == 'i'.upper():
        item_lista = input('Digite o item a ser adicionado: ')
        if item_lista:
            lista_compras.append(item_lista)
        else:
            print('Nenhum item adicionado')
            continue
    elif opcao == 'a'.upper():
        indice_lista = input('Digite o indice: ')
        try:
            indice_lista = int(indice_lista)
            item_apagado = lista_compras.pop(indice_lista)
            print(f'item "{item_apagado} apagado com sucesso.')
        except:
            print('Digite um índice válido')            
    else:
        print('Digite uma opção válida')
        continue

################### CÓDIGO DO PROFESSOR, VER AS EXCEPTIONS:
# import os

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('clear')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         indice_str = input(
#             'Escolha o índice para apagar: '
#         )

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite número int.')
#         except IndexError:
#             print('Índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
#     elif opcao == 'l':
#         os.system('clear')

#         if len(lista) == 0:
#             print('Nada para listar')

#         for i, valor in enumerate(lista):
#             print(i, valor)
#     else:
#         print('Por favor, escolha i, a ou l.')