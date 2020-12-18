def main():
    stringa1 = "abfsfc"
    stringa2 = "sdunvèoasi"
    listaStringa = [stringa1, stringa2]
    listaSet = []

    for indexStringa in range(len(listaStringa)):
        listaSet.append({listaStringa[indexStringa][0]})
        for indexChr in range(1, len(listaStringa[indexStringa])):
            listaSet[indexStringa].add(listaStringa[indexStringa][indexChr])

    paroleComuni = listaSet[0].copy()
    paroleComuni.intersection_update(listaSet[1])
    print(paroleComuni)

    paroleDifferenza = listaSet[0].copy()
    paroleDifferenza.difference_update(listaSet[1])
    print(paroleDifferenza)

    paroleDifferenzaSimmetrica = listaSet[0].copy()
    paroleDifferenzaSimmetrica.symmetric_difference_update(listaSet[1])
    print(paroleDifferenzaSimmetrica)


main()
