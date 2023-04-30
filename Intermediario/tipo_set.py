# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Criando um set
# pode ser assim
s1 = set()  # vazio
#ou assim (parece um dicionário mas não tem chave e valor, só as chaves e itens dentro)
s1 = {'Luiz', 1, 2, 3}  # com dados

s1 = set('Mar') # o print disso vai ser  {'m', 'a', 'r'} e nem sempre na mesma ordem

# os Sets removem vaores iguais automaticamente:
lista = [1,2,3,3,3,3,2,1]
set1 = set(lista) # o set1 vai ficar só com {1,2,3}
lista1 = list(set1) # volta a ser uma lista com [1,2,3] só que pode não ficar na ordem.

# Métodos úteis:
# add, update, clear, discard

# Adicionar:
set2 = set()
set2.add('teste') # com add ele adicionar a palavra inteira, diferente do update
set2.add('teste1')
set2.add('teste2')

#update
set2.update('toller') # assim ele vai adicionar 't', 'o', 'l', 'l', 'e', 'r'
set2.update(('toller', 1,2,3,6))# assim ele adiciona a palavra toda pois esta adicionando uma tupla, assim posso mandar város valores

#clear
set2.clear() # limpa todos os valores

#Discard
set2.discard(1) # aqu tem que dizer o valor que se quer eliminar pois não tem indice

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}

# unir
s3 = s1 | s2 # assim vai ficar {1,2,3,4}

# intersecção:  retorna os iten em comum entre os sets
s4 = s1 & s2 # vai retornar {2,3}

# diferença - Itens presentes apenas no set da esquerda!
s5 = s1 - s2 # vai retornar {1}
s5 = s2 - s1 # neste caso seria {4}

# diferença simétrica ^ - Itens que não estão em ambos
s5 = s1 ^ s2 # vai retornar {1,4} poi estes são itens únicos em cada conjunto. Não importa a ordem
