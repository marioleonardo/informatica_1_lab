import random as rd
import time

rd.seed(time.time())


def main():
    tabella = creaTabellaRandom(5, 4)
    printTabella(tabella)
    print()
    printTabella(neighborAverage(tabella))


def creaTabellaRandom(c, r):
    tabella = [[rd.randint(1, 100) for i in range(c)] for i in range(r)]
    return tabella


def printTabella(tabella):
    for l in tabella:
        print(l)


def neighborAverage(tabella):
    newTabella = creaTabellaRandom(len(tabella[0]), len(tabella))
    for row in range(len(tabella)):
        for column in range(len(tabella[row])):
            elementi = []
            for rowDelta in range(-1, 2):
                for columnDelta in range(-1, 2):
                    if (row + rowDelta in range(0, len(tabella))) and \
                            (column + columnDelta in range(0, len(tabella[row]))) and \
                            (rowDelta * 10 + columnDelta * 100 != 0):
                        elementi.append(tabella[row + rowDelta][column + columnDelta])
            newTabella[row][column] = int(sum(elementi) / len(elementi))
    return newTabella


main()
