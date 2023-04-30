
import os

perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?' ,
        'alternativas': ('1','2','3','4','5', '8', '12'),
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é a raiz de 144?' ,
        'alternativas': ('12','45','10','23','44'),
        'resposta': '12',
    },
    {
        'pergunta': 'Qual o maior ladrão da história do Brasil?' ,
        'alternativas': ('João','Pedro','Lula', 'Maria', 'José'),
        'resposta': 'Lula',
    },
]

opcoes = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
quantidade_perguntas = len(perguntas)
perguntas_corretas = 0


def RetornaPerguntaFormatada(dados_pergunta):
    pergunta = dados_pergunta.get('pergunta')+'\n'
    alternativas =  dados_pergunta.get('alternativas')
    for indice, alternativa in enumerate(alternativas):
        pergunta += opcoes[indice]+') - '+ alternativa+'\n'
    pergunta += 'Digite a opção correta: '
    return pergunta

def MotraRespostaCertaOuErrada(certa):
    global perguntas_corretas
    certa_errada = 'ERRADA ❌'
    if certa:
        certa_errada = 'CORRETA 👍' # não sei como colocar, copiei e colei do professor
        perguntas_corretas += 1        
    print('\r\n', f'************ RESPOSTA {certa_errada} ************', end='\r\n'*2)

for pergunta in perguntas:    
    while True:       
        alternativa_escolhida = input(RetornaPerguntaFormatada(pergunta))
        opcoes_pergunta = opcoes[:len(pergunta.get('alternativas'))]
        os.system('cls')
        if not alternativa_escolhida.lower() in opcoes_pergunta:
            print(f'Opção inválida, digite uma letra entre "{opcoes[0]}" e "{opcoes_pergunta[-1]}"')
            continue

        for indice, letra in enumerate(opcoes):
            if letra == alternativa_escolhida.lower():
                MotraRespostaCertaOuErrada(pergunta.get('resposta') == pergunta.get('alternativas')[indice])
                
        break

print(f'##################### VOCÊ ACERTOU {perguntas_corretas} DE {quantidade_perguntas} PERGUNTAS #####################', end='\r\n'*4)  



########################## CÓDIGO DO PROFESSOR ############################
# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')