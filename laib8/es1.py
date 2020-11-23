import random as rd
import time

rd.seed(time.time())


def main():
    lista1 = [rd.randint(1, 100) for i in range(13)]
    lista2 = [rd.randint(1, 100) for i in range(10)]
    print(lista1)
    print(lista2)
    print(merge(lista1, lista2))


def merge(lista1, lista2):
    lista3 = list()
    listFinished = False
    for index in range(max(len(lista1), len(lista2))):
        if (index < len(lista2) and index < len(lista1)) and (not listFinished):
            lista3.append(lista1[index])
            lista3.append(lista2[index])
        elif (not listFinished):
            listFinished = True
            if len(lista1) > len(lista2):
                lista3 = lista3 + lista1[index:]
            else:
                lista3 = lista3 + lista2[index:]
    return lista3


main()
