def main():
    string = input("Inserisci files separati da virgola:\n")
    parola = input("Inserisci parola da cercare:\n")
    parola = parola.lower()
    parola = parola.strip()
    string = string.replace(" ", "")
    listaNomiFiles = string.split(",")
    listaFiles = []
    for i in listaNomiFiles:
        file = open(i, 'r')
        listaFiles.append(file)

    for fileIndex in range(len(listaFiles)):
        for linea in listaFiles[fileIndex]:
            lineaMinuscola = linea.lower()
            if lineaMinuscola.find(parola) > -1:
                print(listaNomiFiles[fileIndex] + ": " + linea.strip())
        listaFiles[fileIndex].close()


main()
