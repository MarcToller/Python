

#################### VER TB O ARQUIVO formatacao.py
#################### VER TB O ARQUIVO f_strings.py


# temos outra forma de formatar bem parecida com a do Delphi:
# s - string
# d e i int
# f - float
# x e X - Hexadecimal

sobrenome = 'Toller'
idade = 43
salario = 6000.4526
frase = 'Marcelo %s tem %i anos e ganha %f' % (sobrenome, idade, salario) # se for só um valor não precisa de parenteses

#formatar casas decimais:
frase = 'Marcelo %s tem %i anos e ganha %.2f' % (sobrenome, idade, salario) # se for só um valor não precisa de parenteses
print(frase)

print('o exadecimal de %i é %x' % (15, 15)) # x minúsculo mosttra em minúsculo e o X mostra em maiúsculo
print('o exadecimal de %i é %04x' % (15, 15)) # s adicionar um 0 e o numero de digitos ele formata: 000f



