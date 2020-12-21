FILE = "es1input.txt"


def main():
    numeroStanzePrenotate, listaStanzePrenotate = handleInputUser()
    listaStanze, numeroStanze = handleInputFile(FILE)
    prenotaCamere(listaStanzePrenotate, listaStanze)
    updateFile(FILE, listaStanze, numeroStanze)


def handleInputUser():
    numeroStanzePrenotate = int(input("Quante stanze vuoi prenotare? "))
    listaStanzePrenotate = []
    for num in range(numeroStanzePrenotate):
        temp = input(f"Dimensione stanza {str(num + 1)}: ")
        listaStanzePrenotate.append(int(temp))
    return (numeroStanzePrenotate, listaStanzePrenotate)


def handleInputFile(FILE):
    file = open(FILE, "r")
    numeroStanze = file.readline()
    numeroStanze = int(numeroStanze.strip())
    listaStanze = []
    for line in file:
        listaTemp = line.split()
        dictStanza = {"idStanza": int(listaTemp[0]), "capienza": int(listaTemp[1]), "prenotata": int(listaTemp[2])}
        listaStanze.append(dictStanza)
    file.close()
    return (listaStanze, numeroStanze)


def prenotaCamere(listaStanzePrenotate, listaStanze):
    for personePerStanza in listaStanzePrenotate:
        doneFlag = False
        for dictStanza in listaStanze:
            if dictStanza["capienza"] == personePerStanza and not dictStanza["prenotata"] and not doneFlag:
                dictStanza["prenotata"] = 1
                print(f"Camera {dictStanza['idStanza']} – {personePerStanza} persone")
                doneFlag = True
        if not doneFlag:
            print(f"Non è stato possibile fornire la stanza con capienza {personePerStanza} persone")


def updateFile(FILE, listaStanze, numeroStanze):
    file = open(FILE, "w")
    text = f"{len(listaStanze)}\n"
    for dictStanza in listaStanze:
        text += " ".join([str(value) for value in dictStanza.values()]) + "\n"
    file.write(text)
    file.close()


main()
