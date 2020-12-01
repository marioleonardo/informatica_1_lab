import random as rd
import time

rd.seed(time.time())


def main():
    lettura1 = input("cifra:\n")
    lista1 = []
    lista2 = []
    while lettura1 != "0":
        lettura2 = input("nome:\n")
        lista1.append(float(lettura1.strip()))
        lista2.append(lettura2.strip())
        lettura1 = input("cifra:\n")
    print("\nBest customer is", nameOfBestCustomer(lista1, lista2))


def nameOfBestCustomer(lista1, lista2):
    index = lista1.index(max(lista1))
    name = lista2[index]
    return name


main()
