import random

numero_sorteado = random.randint(1,1000)

while True:
    numero_digitado = input('Tente adivinhar, digite um número: ')    
    
    try:
        numero_digitado = int(numero_digitado)              
        if numero_digitado < numero_sorteado:
            print('O número sorteado é maior que o número digitado')
        elif numero_digitado > numero_sorteado:        
            print('O número sorteado é menor que o número digitado')
        else:
            print(f'Você acertou o número ({numero_sorteado}), parabéns.')
            break
    except:
        print(f'O número era {numero_sorteado}')
        break
    