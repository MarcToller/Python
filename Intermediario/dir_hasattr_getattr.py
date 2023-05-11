
# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

print(dir(string)) # mostra todos os métodos disponíveis para este tipo de variável

# Para sab se existe determinado método:
if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string, metodo)()) # aqui ele "aplica" este método! como se fosse um rtti!
else:
    print('Não existe o método', metodo)