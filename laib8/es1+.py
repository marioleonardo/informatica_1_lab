def pariPiuGrande(lista):
    numero = -1
    for i in lista:
        if i % 2 == 0 and i > numero:
            numero = i
    return numero


lista = [1, 7, 65, 3]
print(pariPiuGrande(lista))
