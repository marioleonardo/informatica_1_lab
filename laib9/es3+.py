dimension = 7

lista = []
i = 1
for row in range(dimension):
    lista.append([])
    for column in range(dimension):
        lista[row].append(i)
        i += 1

for row in range(dimension):
    for column in range(dimension):
        print("%3s" % (str(lista[row][column])), end=" ")
    print()
