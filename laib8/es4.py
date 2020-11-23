lista1 = [1, 4, 9, 16, 9, 7, 4, 9, 11, 9]
lista2 = [11, 11, 7, 9, 16, 4, 1, 7]


# def sameSet(lista1, lista2):
#     condition = True
#     for num in lista1:
#         try:
#             lista2.index(num)
#         except:
#             condition = False
#     for num in lista2:
#         try:
#             lista1.index(num)
#         except:
#             condition = False
#     return condition

def sameSet(lista1, lista2):
    togliDuplicati(lista1)
    togliDuplicati(lista2)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False


def togliDuplicati(lista):
    for num in lista:
        for i in range(lista.count(num) - 1):
            lista.remove(num)
    return lista


print(sameSet(lista1, lista2))
