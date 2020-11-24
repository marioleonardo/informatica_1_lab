import random as rd
import time

rd.seed(time.time())


def main():
    values = [16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1]
    dimension = 4
    print(testQuadratoMagico(values, dimension))


def creaTabellaRandom(c, r):
    tabella = [[rd.randint(1, 100) for i in range(c)] for i in range(r)]
    return tabella


def printTabella(tabella):
    for l in tabella:
        print(l)


def testQuadratoMagico(values, dimension):
    errore = ""
    tabella = creaTabellaRandom(dimension, dimension)
    for row in range(dimension):
        for column in range(dimension):
            tabella[row][column] = values[row * dimension + column]
    printTabella(tabella)
    flag = True
    # tutti i numeri?
    for num in range(1, dimension ** 2):
        flag = num in values
        if flag == False:
            errore = "numeri sbagliati"
    # cicliamo
    for row in range(dimension):
        # somma riga==34?
        if sum(tabella[row]) != int(((1 + dimension ** 2) * dimension ** 2) / (2 * dimension)):
            flag = False
            errore = "riga"
        # somma colonne== 34? Abiamo scambiato righe e colonne
        sommaColonne = 0
        for column in range(dimension):
            sommaColonne += tabella[column][row]
        if sommaColonne != int(((1 + dimension ** 2) * dimension ** 2) / (2 * dimension)):
            flag = False
            errore = "colonna"
    return flag, errore


main()
