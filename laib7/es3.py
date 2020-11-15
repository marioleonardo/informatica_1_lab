import random as rd
import time

rd.seed(time.time())

lista1 = [rd.randint(1, 100) for i in range(10)]
lista2 = [rd.randint(1, 100) for i in range(10)]
lista3 = [rd.randint(1, 100) for i in range(10)]
lista4 = lista3.copy()

lista4.insert(0, 0)


def equals(lista1, lista2):
    if len(lista1) > len(lista2):
        lista1, lista2 = lista2, lista1
    print(lista1)
    print(lista2)
    n = 0
    for i in range(len(lista2)):
        if lista2[i] == lista1[n]:
            n += 1
        else:
            n = 0
        if n == len(lista1) - 1:
            return True
    return False


print(equals(lista1, lista2))
print(equals(lista3, lista4))
