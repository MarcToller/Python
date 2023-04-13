vNome = 'Marcelo'
vPeso = 95
vAltura = 1.80

vImc = vPeso / (vAltura ** 2)

print(vNome, 'tem', vAltura, 'de altura')
print('pesa', vPeso, 'quilos e seu IMC é', vImc)
print('ou')
print(f'{vNome} tem {vAltura} de altura')
print(f'pesa {vPeso} quilos e seu IMC é {vImc}')

# para formatar casas decimais no format:
# utiliza-se dois pontos, depois ponto, a quantidade de casas decimais e a letra f:
print(f'pesa {vPeso} quilos e seu IMC é {vImc:.2f}')
# dá para colocar o separador de milhar tb, mas só no formato americano..:
vMilhar = 1000.45
print(f'{vMilhar:,.2f}')

