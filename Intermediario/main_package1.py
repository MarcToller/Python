
from sys import path

#import package1 # só o package inportado não quer dizer nada pois ele é só um caontainer, uma pasta..

# uma das formas seria:
# from package1.modulo1 import soma_do_modulo
# print(soma_do_modulo(1,2))

# ou assim: mas daí dica com os namespaces:
# import package1.modulo1
# print(package1.modulo1.soma_do_modulo(1,2))

# tem a má prática:
# from package1.modulo1 import *
# print(soma_do_modulo(1,2))

#ou assim, como namespace menor:
from package1 import modulo1
print(modulo1.soma_do_modulo(1,2))


################ VAI DAR UM PROBLEMA AQUI POIS EU ESTOU IMPORTANDO O MODULO1 DO PACKAGE E LÁ NO MODULO1 IMPORTO O
################ MODULO2 E EXECUTO UMA FUNÇÃO DELE, ISSO ACONTECE POIS TESE AQUI É O MAIN E O PONTO DE VISTA MUDA
################ POIS O MAIN NÃO CONHECE O MODULO2
################ PARA FUNCIONAR, NO MODULO1 TENHO QUE IMPORTAR ASSIM import package1.modulo2, VAI FUNCIONAR NO
################ MAIN, MAS NÃO VAI FUNCIONAR LÁ NO MODULO1, JUSTAMENTE POR CAUSA DO PONTO DE VISTA


print(*path, sep='\n') # para ver os caminhos que estão no path, podemos alterar e incluir mais caminhos que estejam até fora do nosso escopo, mas só se precisar mesmo..
print(__name__) # mostra que ele é p main