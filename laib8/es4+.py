dimension = 4

lista = []
i = 1
for row in range(dimension):
    lista.append([])
    for column in range(dimension):
        if row % 2 == 0:
            lista[row].append(i)
        else:
            lista[row].insert(0, i)
        i += 1

for row in range(dimension):
    for column in range(dimension):
        print("%3s" % (str(lista[row][column])), end=" ")
    print()
