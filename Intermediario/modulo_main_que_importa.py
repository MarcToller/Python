# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import importlib # este módulo contem a rotina para poder "recarregar um módulo importado
# por que "recarregar"? porque cada módulo importado é um singleton!! E sempre fica vivo, mas se por algum motivo 
# seja necessário "destruir" e "recriar" ele, usamos um método

import modulo_importado
# from modulo_importado import variavel_teste

print('Este módulo se chama', __name__)
print(modulo_importado.variavel_teste)
#print(variavel_teste) usando o from

# recarregando o módulo:
importlib.reload(modulo_importado)
# quando um módulo é importado ele automaticamente executa tudo que ele contem, se tiver um print solto, ele vai printar assim que importado, e se eu tentar importar novamente nada vai acontecer pois ele já esta "vivo" por ser um singleton
# o reload faz ele executar novamente tudo que tem nels
