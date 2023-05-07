try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__) # para saber qual classe é a exceptiom
    print(e )# aqui mostra só a mnsagem da exception
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro') # esse else vai ser executado se não der denhum exceção
finally: # esse é a mesma ideia do delphi
    print('FECHAR ARQUIVO') 