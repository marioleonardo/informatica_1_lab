from operator import itemgetter


def main():
    listaPresenze = generaListaPresenze()
    listaSospettati = generaListaSospettati()
    printContatti(listaPresenze, listaSospettati)


def generaListaPresenze():
    listaPresenze = []
    filePresenze = open("presenze.txt", "r")
    for line in filePresenze:
        listaAttributi = line.split(",")
        cliente = generaDictCliente(listaPresenze, listaAttributi)
        listaPresenze.append(cliente)

    filePresenze.close()
    listaPresenze.sort(key=itemgetter("nome"))
    return listaPresenze


def generaListaSospettati():
    listaSospettati = []
    fileSospetti = open("sospetti.txt", "r")
    for line in fileSospetti:
        sospettato = line.strip()
        listaSospettati.append(sospettato)
    fileSospetti.close()
    return listaSospettati


def printContatti(listaPresenze, listaSospettati):
    for sospettato in listaSospettati:
        print(f"** Contatti del cliente: {sospettato}: **")
        for cliente in listaPresenze:
            if cliente["nome"] == sospettato:
                giorniPermanenzaSospettato = cliente["giorni"]

        almenoUnContatto = False
        for cliente in listaPresenze:
            if (cliente["nome"] != sospettato) and not (cliente["giorni"].isdisjoint(giorniPermanenzaSospettato)):
                print(f"\tContatto con {cliente['nome']}, telefono  {cliente['cellulare']}")
                almenoUnContatto = True

        if not almenoUnContatto:
            print(f"\t{sospettato} non ha avuto contatti con altri clienti")


def generaDictCliente(listaPresenze, listaAttributi):
    for indexAttributo in range(len(listaAttributi)):
        listaAttributi[indexAttributo] = listaAttributi[indexAttributo].strip()
    cliente = {"nome": listaAttributi[0], "cellulare": listaAttributi[1],
               "giorni": set(range(int(listaAttributi[2]), int(listaAttributi[3]) + 1))}
    return cliente


main()
