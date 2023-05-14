
# este módulo que esta dentro do package1 servira de chamada no módulo que esta na raiz, que será o meu main, nomei ele de main_package1.ý


# isto permite que somente o que eu quiser seja inportado deste módulo em outro quando for usado o 
# from modulo import *
__all__ = [
    'teste1',
    'teste4',
    'soma_do_modulo',
]

import package1.modulo2

package1.modulo2.funcao_do_modulo_2()

def soma_do_modulo(x, y):
    return x + y

variavel1 = 'teste1'
variavel2 = 'teste2'
variavel3 = 'teste3'
variavel4 = 'teste4'
