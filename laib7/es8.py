import random as rd
import time

rd.seed(time.time())


def main():
    lista = [rd.randint(80, 100) for i in range(10)]
    oldLista = lista.copy()
    print(lista)
    minimizzaErrore(lista)
    print(lista)

    print(minimizzaErrore_2(lista))
    newLista = minimizzaErrore_2(lista)
    print([(oldLista[i] - lista[i]) for i in range(len(lista))])
    print([(oldLista[i] - newLista[i]) for i in range(len(newLista))])


def minimizzaErrore(lista):
    for index, num in enumerate(lista):
        if index != 0 and index != (len(lista) - 1):
            avg = ((lista[index - 1] + lista[index] + lista[index + 1]) / 3)
        elif index == 0:
            avg = ((lista[index] + lista[index + 1]) / 2)
        else:
            avg = ((lista[index - 1] + lista[index]) / 2)
        avg = int(avg)
        lista.pop(index)
        lista.insert(index, avg)


def minimizzaErrore_2(lista):
    listaNew = []
    for index, num in enumerate(lista):
        if index != 0 and index != (len(lista) - 1):
            avg = ((lista[index - 1] + lista[index] + lista[index + 1]) / 3)
        elif index == 0:
            avg = ((lista[index] + lista[index + 1]) / 2)
        else:
            avg = ((lista[index - 1] + lista[index]) / 2)
        avg = int(avg)
        listaNew.append(avg)
    return listaNew


if __name__ == "__main__":
    main()
