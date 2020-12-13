def main():
    stingaListaClassi = "es7classes.txt"
    studenteId = input("studenteId?\n")
    print("\nstudenteID", studenteId)
    listaVoti = []
    listaClassiVoti = []
    fileListaClassi = open(stingaListaClassi, "r")
    listaStringaClassi = []
    listaClassi = []
    line = fileListaClassi.readline()
    index = 0
    while line != "":
        line = line.strip()
        listaStringaClassi.append(line)
        try:
            listaClassi.append(open("es7" + line + ".txt", "r"))
        except:
            print("wrong file at line", index + 1)
        line = fileListaClassi.readline()
        index += 1

    for indexClassi in range(len(listaClassi)):
        line = listaClassi[indexClassi].readline()
        while line != "":
            listaElementsLine = line.split()
            if listaElementsLine[0] == studenteId:
                listaVoti.append(listaElementsLine[1])
                listaClassiVoti.append(listaStringaClassi[indexClassi])
            line = listaClassi[indexClassi].readline()

    for index in range(len(listaVoti)):
        print(listaClassiVoti[index], listaVoti[index])


main()
