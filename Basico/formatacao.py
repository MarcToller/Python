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

# FORMAT
a = 'A'
b = 'B'
c = 1.1;
format = 'a={} b={} c={:.2f}'
formato = format.format(a,b,c) # lembra o format do Delphi
print(formato)

# posso passar os indices nas chaves, assim não precisa estar na ordem, possoa té repetir!:
format = 'a={0} a={0} a={0} b={1} c={2:.2f}'
formato = format.format(a,b,c) # lembra o format do Delphi
print(formato)

#parametro nomeado
format = 'a={nome0} a={nome0} a={nome0} b={nome1} c={nome2:.2f}'
formato = format.format(nome0=a, nome1=b, nome2=c) # lembra o format do Delphi
print(formato)
