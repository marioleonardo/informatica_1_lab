import random as rd
import time

rd.seed(time.time())


def main():
    lista = [rd.randint(0, 100) for i in range(10)]
    print(lista)
    print(lista[::-1])
    print(inverti(lista))
    print(inverti_2(lista))


def inverti(lista):
    return [lista[len(lista) - 1 - i] for i in range(len(lista))]


def inverti_2(lista):
    listaNew = []
    for i in lista:
        listaNew.insert(0, i)
    return listaNew


if __name__ == "__main__":
    main()
