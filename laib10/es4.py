def main():
    string = "es4input.txt"
    string = string.replace(" ", "")
    listaAttributi = ["user", "categoria", "importo", "data"]

    try:
        file = open(string, 'r')
    except:
        print("file not correct")
        return

    matrix = []
    line = file.readline()
    while line != "":
        lista = line.split(";")
        for indexElement in range(len(lista)):
            lista[indexElement] = lista[indexElement].strip()
            lista[indexElement] = lista[indexElement].lower()
        matrix.append(lista)
        line = file.readline()

    categories = []
    categoriesTotal = []
    for indexLine in range(len(matrix)):
        for indexElement in range(len(matrix[indexLine])):
            if listaAttributi[indexElement] == "importo":
                importo = float(matrix[indexLine][indexElement])
            if listaAttributi[indexElement] == "categoria":
                categoria = matrix[indexLine][indexElement]
        totalAdd(categoria, importo, categories, categoriesTotal)

    for indexCategory in range(len(categories)):
        print(categories[indexCategory] + ": " + "%.2f" % (categoriesTotal[indexCategory]))
    file.close()


def totalAdd(categoria, importo, categories, categoriesTotal):
    flagImportoAdded = False
    for categoryIndex in range(len(categories)):
        if categoria == categories[categoryIndex]:
            categoriesTotal[categoryIndex] += importo
            flagImportoAdded = True

    if flagImportoAdded == False:
        categories.append(categoria)
        categoriesTotal.append(importo)


main()
