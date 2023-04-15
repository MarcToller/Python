"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
[i:f:p] inicio, final, passo (de quantos em quantos)
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:8]) # vamos pergar da sring 4 até a 7 (sim tem que colocar um a mais) vai mostrar mund 
print(variavel[4:]) # assim vai do 4 até o final
print(variavel[0:5]) # vai no 0 a 4: Olá m
print(variavel[:5]) # Omitindo o inicio vai no 0 a 4 tb: Olá m
print(variavel[::-1]) # omiti o inicio e fim então ele vai considerar toda a sring, mas o passo -1 vai fazer ele inverter toda a string
print(variavel[-1:-10:-1]) # este tem o mesmo efeito do de cima, mas informando os indices de inicio -1 e fim -10(sempre um a mais no final) e voltando sempre -1
