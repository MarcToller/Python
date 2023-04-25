"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1
h = 2

def escopo():
    global x # este global faz com que o x lá de cima seja manipulado pois tem o mesmo nome entãao se torna a mesma váriável!!
    x = 10
    h = 3 # se eu não tivesse esse h, no print de baixo ele usaia o h de fora (h = 2)

    def outra_funcao(): # posso ter funcao dentro de funcao!
        global x #mesmo caso do glogal de cima. Sem o global esse x é outra variável que esta somente no escopo do submetodo
        x = 11
        y = 2
        h = 4 # se eu não tivesse esse h, no print de baixo ele usaia o h de cima (h = 3)
        print(x, y, h)

    outra_funcao()
    print(x, h)


print('x = 1:', x) # este x é o do modulo, ou seja o 1 lá de cima
escopo()
print('x = 11:', x) # este x é o do modulo, ou seja o 1 lá de cima
