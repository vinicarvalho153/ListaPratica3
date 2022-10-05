lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
valorRepetidos = set()
valor = []

for lista in lista:
    if lista not in valor:
        valor.append(lista)
    else:
        valorRepetidos.add(lista)
print(valorRepetidos)