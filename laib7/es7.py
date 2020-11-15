import random as rd
import time

rd.seed(time.time())


def main():
    lista = [rd.randint(0, 100) for i in range(10)]
    print(lista)
    print(somma(lista))
    print(operazioneStrana(lista))
    print(operazioneStrana_2(lista))


def operazioneStrana(lista):
    minimo = lista[0]
    somma = 0
    for num in lista:
        minimo = min(minimo, num)
        somma += num
    somma = somma - minimo
    return somma


def operazioneStrana_2(lista):
    lista.sort()
    lista.pop(0)
    return (somma(lista))


def somma(lista):
    somma = 0
    for num in lista:
        somma += num
    return somma


if __name__ == "__main__":
    main()
