def main():
    LENGTH_MATRIX = 50
    HEIGHT_MATRIX = 50

    matrix = createMatrix(LENGTH_MATRIX, HEIGHT_MATRIX)
    printMatrix(matrix)

    instruction = input("\nQuale operazione?\n")
    while instruction != "0":
        instructionList = instruction.split()
        modifyMatrix(matrix, instructionList)
        printMatrix(matrix)

        instruction = input("\nQuale operazione?\n")


def createMatrix(length, height):
    matrix = []
    for r in range(height):
        line = []
        for c in range(length):
            line.append(".")
        matrix.append(line)
    return matrix


def modifyMatrix(matrix, instructionList):
    c = int(instructionList[1])
    r = int(instructionList[2])
    if r >= len(matrix) or c >= len(matrix[0]):
        raise ("errore coordinate")

    if instructionList[0].lower() == "p":
        matrix[r].insert(c, "*")

    elif instructionList[0].lower() == "h":
        length = int(instructionList[3])
        for index in range(length):
            if r < len(matrix) and (c + index) < len(matrix[0]):
                if matrix[r][c + index] != "|":
                    matrix[r][c + index] = "-"
                else:
                    matrix[r][c + index] = "+"
    elif instructionList[0].lower() == "v":
        length = int(instructionList[3])
        for index in range(length):
            if r + index < len(matrix) and (c) < len(matrix[0]):
                if matrix[r + index][c] != "-":
                    matrix[r + index][c] = "|"
                else:
                    matrix[r + index][c] = "+"
    else:
        raise ("istruzione errore")


def printMatrix(matrix):
    file = open("es4output.txt", "w")
    text = ""
    for indexR in range(len(matrix)):
        for indexC in range(len(matrix[0])):
            text += matrix[len(matrix) - 1 - indexR][indexC] + " "
        text += "\n"
    file.write(text)
    file.close()


main()
