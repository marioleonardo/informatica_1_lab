def main():
    turno = 0
    lista = [[" " for i in range(3)] for i in range(3)]

    while (turno != -1):
        print(f"  A B C\n1 {' '.join(lista[0])}\n2 {' '.join(lista[1])}\n3 {' '.join(lista[2])}\n")
        if turno == 0:
            print("E' il turno del giocatore croce")
            turno = modificaCasella(input("inserisci casella: ".lower()), "X", lista, turno)
        else:
            print("E' il turno del giocatore cerchio")
            turno = modificaCasella(input("inserisci casella: ".lower()), "O", lista, turno)
        turno = checkWin(lista, turno)


def modificaCasella(str, emoticon, lista, turno):
    try:
        if lista[int(str[1]) - 1][ord(str[0]) - ord("a")] == " ":
            lista[int(str[1]) - 1][ord(str[0]) - ord("a")] = emoticon
            turno = 1 if turno == 0 else 0
    except:
        print("errore")
    return turno


def checkWin(lista, turno):
    listaLineare = []

    for row in range(3):
        colonna = []
        riga = lista[row]
        for column in range(3):
            colonna.append(lista[column][row])
            listaLineare.append(lista[row][column])
        if (riga == ["X"] * 3 or riga == ["O"] * 3) or (colonna == ["X"] * 3 or colonna == ["O"] * 3):
            giocatore = "crocetta" if turno == 1 else "cerchio"
            print(f"\nil vincitore è {giocatore}")
            turno = -1

    diagonale1 = []
    diagonale2 = []
    for i in range(3):
        diagonale1.append(lista[i][i])
        diagonale2.append(lista[i][2 - i])
    if diagonale1 == ["X"] * 3 or diagonale1 == ["O"] * 3 or diagonale2 == ["X"] * 3 or diagonale2 == ["O"] * 3:
        giocatore = "crocetta" if turno == 0 else "cerchio"
        print(f"\nil vincitore è {giocatore}")
        turno = -1
        
    if " " not in listaLineare:
        print("\nNessun vincitore")
        turno = -1
    return turno


if __name__ == "__main__":
    main()
