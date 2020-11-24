import random as rd
import time

rd.seed(time.time())


def main():
    lista1 = [rd.randint(1, 100) for i in range(13)]
    lista2 = [rd.randint(1, 100) for i in range(17)]
    lista1.sort()
    lista2.sort()
    print(lista1)
    print(lista2)
    print(mergeSorted(lista1, lista2))
    # confronto
    lista1 = lista1 + lista2
    lista1.sort()
    print(lista1)


def mergeSorted(lista1, lista2):
    newList = []
    indexLista1 = 0
    indexLista2 = 0
    for index in range(len(lista1) + len(lista2)):
        if ((lista1[indexLista1] < lista2[indexLista2]) or (indexLista2 == -1)) and \
                (indexLista1 != - 1):
            newList.append(lista1[indexLista1])
            indexLista1 = indexLista1 + 1 if indexLista1 != len(lista1) - 1 else -1
        else:
            newList.append(lista2[indexLista2])
            indexLista2 = indexLista2 + 1 if indexLista2 != len(lista2) - 1 else -1
    return newList


main()
