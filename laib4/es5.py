import math


def isPrimo(num):
    prime = True
    for num2 in range(2, math.floor(math.sqrt(num)) + 1):
        if num % num2 == 0:
            prime = False
    return prime


def numeriPrimi(start, end):
    primeNumbers = []
    while start <= end:
        if isPrimo(start):
            primeNumbers.append(start)
        start = start + 1
    return primeNumbers


print(numeriPrimi(2, int(input("Qual é il numero?\n"))))
