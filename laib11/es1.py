def main():
    file1 = open("es1input.txt", "r")
    file2 = open("es1output.txt", "w")
    line = file1.readline()
    dictParole = {}
    while line != "":
        listaParole = []
        inParola = False
        for indexStringa in range(len(line)):
            if line[indexStringa].isalpha() and not inParola:
                inParola = True
                stringaTemp = line[indexStringa]
            elif line[indexStringa].isalpha() and inParola:
                stringaTemp += line[indexStringa]
            elif not line[indexStringa].isalpha() and inParola:
                inParola = False
                listaParole.append(stringaTemp)

        while len(listaParole) > 0:
            parola = listaParole.pop()
            if parola in dictParole:
                dictParole.update({parola: dictParole[parola] + 1})
            else:
                dictParole.update({parola: 1})

        line = file1.readline()

    stringa = ""
    printableDict = obtainPrintableDict(dictParole, n=100)
    printableDict = {k: v for k, v in sorted(printableDict.items(), reverse=True, key=lambda lista: lista[1])}
    for key, value in printableDict.items():
        stringa = stringa + ("%-12s :   %d\n" % (key, value))

    file2.write(stringa)

    file1.close()
    file2.close()


def obtainPrintableDict(dictParole, n=20):
    if len(dictParole) <= n:
        return dictParole
    else:
        dictParoleNew = {}
        valueMaster = 1
        listaValori = [el for el in dictParole.values() if el >= valueMaster]
        while len(listaValori) > n:
            valueMaster += 1
            listaValori = [el for el in listaValori if el >= valueMaster]

        if len(listaValori) != n:
            valueMaster -= 1

        for key, value in dictParole.items():
            if value >= valueMaster and len(dictParoleNew) < n:
                dictParoleNew[key] = value
        return dictParoleNew


main()
