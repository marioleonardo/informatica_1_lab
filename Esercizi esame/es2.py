import random


def main():
    mazzo = generateMazzo(["7", "8", "9", "10", "J", "Q", "K", "A"], ["C", "Q", "F", "P"])
    mazzo = shuffleMazzo(mazzo)
    print(mazzo)
    try:
        saveMazzo("es2io.txt", mazzo)
    except:
        print("errore salvataggio")
    for i in range(len(mazzo) // 5):
        stampaCombinazione(mazzo[:5])
        mazzo = mazzo[5:]
    stampaCombinazione(["10C", "7C", "QC", "AC", "KC"])


def generateMazzo(valori, semi):
    mazzo = []
    for valore in valori:
        for seme in semi:
            mazzo.append(valore + seme)
    return mazzo


def shuffleMazzo(mazzo):
    mazzoNew = []
    while mazzo != []:
        mazzoNew.append(mazzo.pop(random.randint(0, len(mazzo) - 1)))
    return mazzoNew


def saveMazzo(stringaFile, mazzo):
    print("salvato!")


def stampaCombinazione(mazzo):
    semi = set()
    valori = set()
    listaValori = []
    for element in mazzo:
        semi.add(element[-1])
        valori.add(element[:-1])
        listaValori.append(element[:-1])
    listavaloriUguali = [listaValori.count(listaValori[a]) for a in range(len(listaValori)) if
                         listaValori.count(listaValori[a]) != 1]

    if len(semi) == 1 and valori == {"10", "J", "Q", "K", "A"}:
        string = "in fila (scala reale)"
    elif len(semi) == 1:
        string = "colore"
    elif (listavaloriUguali != [] and max(listavaloriUguali) == 4):
        string = "4 carte uguali (poker)"
    elif (listavaloriUguali != [] and max(listavaloriUguali) == 3):
        string = "3 carte uguali"
    elif (listavaloriUguali.count(2) == 4):
        string = "2 coppie"
    elif (listavaloriUguali != [] and max(listavaloriUguali) == 2):
        string = "2 carte uguali"
    else:
        string = "Niente.."
    print(mazzo, string)


main()
