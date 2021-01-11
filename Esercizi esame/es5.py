import random


def main():
    mazzo = generateMazzo(listaCarte)
    mazzi = splitMazzo(mazzo, 2)
    punteggi = [0, 0]
    puntiTavolo = 0
    index = 0

    index += 1
    print("\nmano n°", index)
    carte = estrazioneCarte(mazzi)
    vincitore, puntiTemp = checkVittoria(carte, listaCarte)
    if vincitore != -1:
        punteggi[vincitore] += puntiTemp + puntiTavolo
        puntiTavolo = 0
    else:
        puntiTavolo += puntiTemp
    printPunteggi(punteggi)


print(f"\nvince il giocatore {punteggi.index(max(punteggi)) + 1} con {max(punteggi)} punti")

listaCarte = [
    {
        "nome": "gialla",
        "punti": 1,
        "numero": 10
    },
    {
        "nome": "verde",
        "punti": 3,
        "numero": 10
    },
    {
        "nome": "rossa",
        "punti": 5,
        "numero": 10
    },
]


def generateMazzo(listaCarte):
    mazzo = []
    for colore in listaCarte:
        mazzo.extend([colore["nome"]] * colore["numero"])
    mazzoShuffled = []
    while mazzo != []:
        mazzoShuffled.append(mazzo.pop(random.randint(0, len(mazzo) - 1)))
    return mazzoShuffled


def splitMazzo(mazzo, numeroMazzi):
    mazzi = [[], []]
    for numero in range(len(mazzo) // numeroMazzi):
        for index in range((numeroMazzi)):
            mazzi[index].append(mazzo.pop(0))
    return mazzi


def estrazioneCarte(mazzi):
    carte = []
    for index, mazzo in enumerate(mazzi):
        carte.append(mazzo.pop(0))
        print(f"carta giocatore {index + 1}: {carte[-1]}")
    return carte


def printPunteggi(punteggi):
    for index, punteggio in enumerate(punteggi):
        print(f"Punteggio giocatore {index + 1}:", punteggio)


def checkVittoria(carte, listaCarte):
    punteggi = []
    for carta in carte:
        for dict in listaCarte:
            if dict["nome"] == carta:
                punteggi.append(dict["punti"])
    punteggioMassimo = max(punteggi)
    if punteggi.count(punteggioMassimo) > 1:
        vincitore = -1
        print("risultato: pareggio")
    else:
        vincitore = punteggi.index(punteggioMassimo)
        print("risultato: vince la mano il giocatore", vincitore + 1)
    return (vincitore, sum(punteggi))


main()
