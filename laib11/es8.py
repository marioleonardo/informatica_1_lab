def main():
    file = open("es8input.txt", "r")
    file2 = open("es8output.txt", "w")
    dictPositions = {}
    text = file.read().lower()
    listaCelle = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dictCoordinate = {(1, 0): "N", (-1, 0): "S", (0, 1): "W", (0, -1): "E"}
    r = 0
    c = 0
    index = 0
    while index < len(text):
        if text[index] == " ":
            position = (int(r), int(c))
            dictPositions.update({position: ""})
        c += 1
        if text[index] == "\n":
            r += 1
            c = 0
        index += 1

    for key in dictPositions:
        rkey, ckey = key
        listaCorridoiVicini = []
        for index in range(4):
            if (rkey + listaCelle[index][0], ckey + listaCelle[index][1]) in dictPositions:
                listaCorridoiVicini.append((rkey + listaCelle[index][0], ckey + listaCelle[index][1]))
        dictPositions[key] = set(listaCorridoiVicini)
    print(dictPositions)

    text = text.replace(" ", "?")

    matrix = []
    righe = text.split("\n")
    for indexRiga in range(len(righe)):
        listaCaratteri = []
        for indexChr in range(len(righe[indexRiga])):
            listaCaratteri.append(righe[indexRiga][indexChr])
        matrix.append(listaCaratteri)

    numeroRighe = len(matrix)
    numeroColonne = len(matrix[0])

    for key in dictPositions:
        rkey, ckey = key
        if rkey == 0:
            matrix[rkey][ckey] = "N"
            matrix = findPath(rkey, ckey, dictPositions, matrix, dictCoordinate)
        if rkey == numeroRighe - 1:
            matrix[rkey][ckey] = "S"
            matrix = findPath(rkey, ckey, dictPositions, matrix, dictCoordinate)
        if ckey == 0:
            matrix[rkey][ckey] = "W"
            matrix = findPath(rkey, ckey, dictPositions, matrix, dictCoordinate)
        if ckey == numeroColonne - 1:
            matrix[rkey][ckey] = "E"
            matrix = findPath(rkey, ckey, dictPositions, matrix, dictCoordinate)

    matrixText = ""
    for lista in matrix:
        for chr in lista:
            matrixText += (chr)
        matrixText += "\n"
    file2.write(matrixText)
    file.close()
    file2.close()


def findPath(rkey, ckey, dictPositions, matrix, dictCoordinate):
    # exitFlag = False
    # while not exitFlag:
    #     exitFlag = True
    listaNeighbours = dictPositions[(rkey, ckey)]
    for element in listaNeighbours:
        r, c = element
        if matrix[r][c] == "?":
            matrix[r][c] = dictCoordinate[(r - rkey, c - ckey)]
            matrix = findPath(r, c, dictPositions, matrix, dictCoordinate)

    return matrix


main()
