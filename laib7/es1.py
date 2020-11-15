import random as rd
import time

rd.seed(time.time())

lista = []

for i in range(10):
    lista.append(rd.randint(1, 100))
print(lista)
lista = [rd.randint(1, 100) for i in range(10)]
print(lista)

print("indice pari")
print(lista[::2])
print([(lista[i]) for i in range(len(lista)) if i % 2 == 0])

print("indice dispari")
print(lista[1::2])
print([(lista[i]) for i in range(len(lista)) if i % 2 != 0])

print("ordine inverso")
print(lista[::-1])

print("primo e ultimo")
print(lista[:1], end=", ")
print(lista[-1:])
