RIGHE = 4
COLONNE = 10


def printTabella(tabella):
    for l in tabella:
        print(l)


lista = []
for i in range(RIGHE):
    lista.append([])
    for j in range(COLONNE):
        lista[i].append(1)
        if i > 0 and j > 0:
            lista[i][j] = lista[i][j - 1] + lista[i - 1][j]

printTabella(lista)
