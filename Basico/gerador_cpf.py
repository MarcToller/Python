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
import random

quantidade_cpfs = int(input('Quantos CPFs deseja gerar? '))
quantidade = 0
cpf_somente_numeros = ''
cpf_gerado = ''

while quantidade <= quantidade_cpfs:
    digito = 1
    cpf_somente_numeros = ''
    cpf_gerado = ''
    while digito <= 9:
        digito += 1   
        cpf_somente_numeros += str(random.randint(0, 9))        
    
    cpf_digito_calculado = 0
    soma_digitos = 0

    for posicao_digito in [10,11]:
        if len(cpf_gerado) == 0:
            cpf_gerado = cpf_somente_numeros[:posicao_digito-1]            

        soma_digitos = 0

        for indice_calculo, digito in enumerate(cpf_gerado, start=posicao_digito*-1):
            soma_digitos += (int(digito) * (indice_calculo*-1)) * 10

        resto = soma_digitos % 11    

        cpf_digito_calculado = resto if resto <= 9 else 0
        cpf_gerado = cpf_gerado + str(cpf_digito_calculado)                 
    quantidade += 1

    print(f'CPF gerado: {cpf_gerado}')