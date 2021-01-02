def main():
    file = open("es3input.txt", "r")
    matrix = []
    for line in file:
        matrix.append(line.split(";"))
    file.close()

    dictRegioni = {}
    dictCitta = {}

    for element in matrix:
        regione = element[10].lower()
        citta = element[11].lower()
        if not dictCitta.get(regione):
            dictCitta[regione] = []
        dictCitta[regione].append(citta)

    for regione in dictCitta:
        numeroComuni = len(dictCitta[regione])
        comuneMax = ""
        comuneMin = dictCitta[regione][0]
        for comune in dictCitta[regione]:
            if len(comune) > len(comuneMax) or ((len(comune) == len(comuneMax)) and comune > comuneMax):
                comuneMax = comune
            if len(comune) < len(comuneMin) or ((len(comune) == len(comuneMin)) and comune < comuneMin):
                comuneMin = comune
        dictRegioni[regione] = [numeroComuni, comuneMin, comuneMax]

    regione = input("\nQuale regione?\n")
    while regione != "***":
        listaRisultati = dictRegioni.get(regione)
        if listaRisultati:
            print("il numero di comuni presenti in tale regione:", listaRisultati[0])
            print("il comune il cui nome ha il numero minimo di caratteri:", listaRisultati[1])
            print("il comune il cui nome ha il numero massimo di caratteri:", listaRisultati[2])
        regione = input("\nQuale regione?\n")


main()
