"""
Calculo do primeiro dígito do CPF                        Calculo do segundo dígito do CPF               
CPF: 746.824.890-70                                      CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF             Colete a soma dos 9 primeiros dígitos do CPF,
multiplicando cada um dos valores por uma                MAIS O PRIMEIRO DIGITO,
contagem regressiva começando de 10                      multiplicando cada um dos valores por uma
Ex.:  746.824.890-70 (746824890)                         contagem regressiva começando de 11
   10  9  8  7  6  5  4  3  2                            Ex.:  746.824.890-70 (7468248907)
*  7   4  6  8  2  4  8  9  0                               11 10  9  8  7  6  5  4  3  2
   70  36 48 56 12 20 32 27 0                            *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
Somar todos os resultados:                                  77 40 54 64 14 24 40 36  0 14
70+36+48+56+12+20+32+27+0 = 301                          Somar todos os resultados:
Multiplicar o resultado anterior por 10                  77+40+54+64+14+24+40+36+0+14 = 363
301 * 10 = 3010                                          Multiplicar o resultado anterior por 10
Obter o resto da divisão da conta anterior por 11        363 * 10 = 3630
3010 % 11 = 7                                            Obter o resto da divisão da conta anterior por 11
Se o resultado anterior for maior que 9:                 3630 % 11 = 0
    resultado é 0                                        Se o resultado anterior for maior que 9:
contrário disso:                                             resultado é 0
    resultado é o valor da conta                         contrário disso:
O primeiro dígito do CPF é 7                                 resultado é o valor da conta
                                                         O segundo dígito do CPF é 0
"""

# importação de expressões regulares
import re
import sys

cpf_completo = input('Digite o cpf: ')
cpf_somente_numeros = ''
cpf_valido = True
cpf_gerado = ''
cpf_digito_calculado = 0
soma_digitos = 0

## remover com expressão regular tudo que não for numeros!!!
cpf_somente_numeros = re.sub( # sub = substituir
    r'[^0-9]', # a expressão regular de busca, tem que colocar o r na frente para indicar que é ER
    '', # valor para sbstituir
    cpf_completo # valor substituido
) 
#print(cpf_somente_numeros)


# for digito in cpf_completo:
#     if not digito in '.-':
#         try:            
#             digito_numerico = int(digito)
#             cpf_somente_numeros += str(digito_numerico)
#         except:
#             cpf_valido = False
#             print('CPF contém caracteres inválidos.')
#             break


cpf_valido = len(cpf_somente_numeros) == 11
if not cpf_valido:
    print('Tamanho do CPF inválido')
    sys.exit() # sai fora do python, como um break

# não pode deixar validar cpfs com numeros todos repetidos:
if cpf_valido:
    primeiro_numero = cpf_somente_numeros[0] 
    cpf_numeros_repetidos = str(primeiro_numero) * len(cpf_somente_numeros)
    cpf_valido = cpf_numeros_repetidos != cpf_completo
    if not cpf_valido:
        print('Não é permitido cpf com números todos iguais')
        sys.exit()

if cpf_valido:
    for posicao_digito in (10,11):
        if len(cpf_gerado) == 0:
            cpf_gerado = cpf_somente_numeros[:posicao_digito-1]            

        soma_digitos = 0

        for indice_calculo, digito in enumerate(cpf_gerado, start=posicao_digito*-1):
            soma_digitos += (int(digito) * (indice_calculo*-1)) * 10

        resto = soma_digitos % 11    

        cpf_digito_calculado = resto if resto <= 9 else 0
        cpf_gerado = cpf_gerado + str(cpf_digito_calculado)     
            
cpf_valido = cpf_gerado == cpf_somente_numeros

if cpf_valido:
    print('CPF válido')                  
else:      
    print('CPF inválido: CPF Digitado: ', cpf_somente_numeros, 'CPF Correto:', cpf_gerado)