import random
import os


ListaDePalavras = ['ovo', 'Carro', 'Casa', 'abacate', 'tomate', 'Computador', 'comida']
JogarDenovo = False

while True:    
    tentativas = 0
    indice = random.randint(1, len(ListaDePalavras)-1)
    PalavraSorteada = ListaDePalavras[indice] 
    AcumuladorLetra = ''
    PalavraSorteada = PalavraSorteada.upper()

    if JogarDenovo:
        JogarDenovo = input('Deseja jogar outra vez? ')
        if JogarDenovo.upper() == 'N':
            break

    while True:        
        tentativas += 1
        letra = input('Digite uma letra: ').upper()

        if len(letra) > 1:
            print('Digite apenas uma letra!')
            continue
        
        if letra in PalavraSorteada and letra not in AcumuladorLetra:
            AcumuladorLetra += letra
        elif letra in AcumuladorLetra:    
            print('Você já digitou esta letra!')    
            continue
        else:
            print('Palavra não tem essa letra!')    
            continue

        PalavraDigitada = ''
        for letra in PalavraSorteada:
            if letra in AcumuladorLetra:
                PalavraDigitada += letra
            else:
                PalavraDigitada += '*' 

        os.system('cls')                             
        print(PalavraDigitada)
        if PalavraDigitada == PalavraSorteada:
            print(f'PARABÉNS, VOCÊ COMPLETOU A PALAVRA EM {tentativas} TENTATIVAS.')
            JogarDenovo = True
            break 
