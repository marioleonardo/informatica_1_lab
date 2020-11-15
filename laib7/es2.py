import random as rd
import time

rd.seed(time.time())

lista = []
risultato = 0

lista = [rd.randint(1, 100) for i in range(10)]
print(lista)
lista = [lista[i - 1] - lista[i] for i, num in enumerate(lista) if i % 2 == 1]
print(lista)
for i in lista:
    risultato += i
print(risultato)
