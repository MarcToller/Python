def divide_lista_em_tres_partes(lista):
    # Calcula todas as diferenças entre valores adjacentes na lista
    ##diferencas = sorted(set([abs(lista[i] - lista[i + 1]) for i in range(len(lista) - 1)]))      
    ##diferencas = sorted(set([abs(lista[i] - lista[i + 1]) for i in range(len(lista) - 1) if abs(lista[i] - lista[i + 1]) != 0]))
    diferencas = sorted(set([dif for i, dif in enumerate([abs(lista[i] - lista[i + 1]) for i in range(len(lista) - 1)]) if dif != 0]))


    print('DIFERENÇAS', diferencas)



    # Ordena as diferenças em ordem decrescente
    diferencas_ordenadas = sorted(enumerate(diferencas), key=lambda x: x[1], reverse=False)
    print('DIFERENÇAS ORDENADAS', diferencas_ordenadas)

    # Pega os índices das duas maiores diferenças
    indice_1, indice_2 = diferencas_ordenadas[0][0], diferencas_ordenadas[1][0]

    # Garante que os índices estejam em ordem crescente
    indice_1, indice_2 = min(indice_1, indice_2), max(indice_1, indice_2)

    # Divide a lista em três partes usando os índices encontrados
    parte1 = lista[:indice_1 + 1]
    parte2 = lista[indice_1 + 1:indice_2 + 1]
    parte3 = lista[indice_2 + 1:]

    return parte1, parte2, parte3

# Exemplo de uso
minha_lista = [18,18,22,23,25,32,33,36,56,60,79,118,120,128,192,263,273,285,303,358,435,583,608,658,1135]
parte1, parte2, parte3 = divide_lista_em_tres_partes(minha_lista)
print("Parte 1:", parte1)
print("Parte 2:", parte2)
print("Parte 3:", parte3)
