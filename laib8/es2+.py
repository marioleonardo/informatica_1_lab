def pariDispari(lista1, lista2, Tipo="Pari"):
    for i in range(len(lista1)):
        if lista2[i] == "pari":
            maxPari = max(lista1[i])
        if lista2[i] == "dispari":
            maxDispari = max(lista1[i])


lista1 = [1, 2, 3, 4, 0, -89]
lista2 = list()

for i in range(len(list)):
    if list[i] % 2 == 0:
        lista2.append("pari")
    else:
        lista2.append("dispari")
print(pariDispari(lista1, lista2))
