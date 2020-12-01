import math
import random as rd


def main():
    lista1 = [rd.randint(1, 100) for i in range(14)]
    lista2 = [rd.randint(1, 100) for i in range(10)]
    print(lista1)
    print(lista2)
    print(scambioPrimoUltimo(lista1))
    print(scorrimentoDestra(lista1))
    print(evenZeroSubstitution(lista1))
    print(maxSubstitution(lista1))
    print(centralElimination(lista1))
    print(evenFrontOddBottom(lista1))
    print(smallerMax(lista1))
    print(testCrescenza([1, 2, 3]))
    print(testDuplicatiAdiacenti(lista1))
    print(testDuplicati(lista1))
    print(removeMin(lista1))  # es4


def scambioPrimoUltimo(lista1):
    lista3 = lista1.copy()
    lista3[0], lista3[-1] = lista3[-1], lista3[0]
    return lista3


def scambioPrimoUltimo2(lista1):
    lista3 = lista1.copy()
    temp = lista3[-1]
    lista3[-1] = lista3[0]
    lista3[0] = temp
    return lista3


def scorrimentoDestra(lista1):
    lista3 = []
    lista3 = lista1[-1:] + lista1[: -1]
    return lista3


def evenZeroSubstitution(lista1):
    lista3 = lista1.copy()
    for i in range(len(lista3)):
        if lista3[i] % 2 == 0:
            lista3[i] = 0
    return lista3


def evenZeroSubstitution(lista1):
    lista3 = lista1.copy()
    for i in range(len(lista3)):
        if lista3[i] % 2 == 0:
            lista3[i] = 0
    return lista3


def maxSubstitution(lista1):
    lista3 = lista1.copy()
    for i in range(1, len(lista3) - 1):
        lista3[i] = max(lista3[i - 1], lista3[i + 1])
    return lista3


def centralElimination(lista1):
    lista3 = lista1.copy()
    lista3[math.ceil(round((len(lista3) - 1) / 2, 1))] = 0
    lista3[math.floor(round((len(lista3) - 1) / 2, 1))] = 0
    return lista3


def evenFrontOddBottom(lista1):
    lista3 = lista1.copy()
    index = len(lista3) - 1
    stop = -1
    while index > stop:
        if lista3[index] % 2 == 0:
            lista3.insert(0, lista3[index])
            lista3.pop(index + 1)
            stop += 1
        else:
            index -= 1
    return lista3


def smallerMax(lista1):
    max2 = min(lista1)
    for num in lista1:
        if num < max(lista1) and num > max2:
            max2 = num
    return max2


def testCrescenza(lista1):
    for index in range(1, len(lista1)):
        if lista1[index] < lista1[index - 1]:
            return False
    return True


def testDuplicatiAdiacenti(lista1):
    for index in range(1, len(lista1)):
        if lista1[index] == lista1[index - 1]:
            return True
    return False


def testDuplicati(lista1):
    for index in range(len(lista1)):
        if lista1.index(lista1[index]) != index:
            return True, lista1[index]
    return False


def removeMin(lista1):
    lista3 = lista1.copy()
    min = lista3[0]
    indexMin = 0
    for index in range(len(lista3)):
        if lista3[index] < min:
            min = lista3[index]
            indexMin = index

    lista3.pop(indexMin)
    return lista3


def merge(a, u):
    return


main()
