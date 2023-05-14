
# tudo que eu colocar neste arquivo ficará disponivel em todo lugar que eu import o package_init (nome que eu inventei), este arquivo é executado assim que o package_init for importado, mas o arquivo deve ter exatamente este nome __init__.py, fica disponível até as importações que eu faço aqui, pois ele importa e exporta, o package acaba se comportando como um modulo!

from package_init.outro_modulo import fala_oi, fala_tchau # se eu importar o package_init em outro módulo, estas funções estarão disponíveis lá chamando o package_init.fala_oi()

# posso fazer assim tb:
from package_init.outro_modulo import *

variavel_do_init = 'variavel_do_init'

# obs.: ao executr esse py vai dar rro por causa do package_init.outro_modulo, ms tudo é o ponto de vista, já no modulo_importa_init.py vai dar certo..



