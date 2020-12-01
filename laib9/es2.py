import random as rd
import time

rd.seed(time.time())


def main():
    tabella = creaTabellaPosti(12, 8)
    printTabella(tabella)
    lettura = input("\nScegli un posto stile battaglia navale oppure scegli un prezzo:\n")
    while lettura != "-1":
        lettura = lettura.upper()
        lettura = lettura.strip()
        if lettura[0].isdecimal():
            flag = True
            for r in range(len(tabella)):
                for c in range(len(tabella[0])):
                    if tabella[r][c] == int(lettura) and flag:
                        print(f"posto {c + 1} riga {r + 1}")
                        flag = False
                        tabella[r][c] = 0
        elif lettura[0].isalpha():
            riga = ord(lettura[0]) - ord("A")
            colonna = int(lettura[1:]) - 1

            if riga >= 0 and riga <= len(tabella) and colonna >= 0 and colonna <= len(tabella[0]):
                if tabella[riga][colonna] != 0:
                    tabella[riga][colonna] = 0
                    print(f"posto {colonna + 1} riga {riga + 1}")
        printTabella(tabella)
        lettura = input("Scegli un posto stile battaglia navale oppure scegli un prezzo:\n")


def creaTabellaPosti(colonne, righe):
    tabella = [[rd.randint(1, 100) for i in range(colonne)] for i in range(righe)]
    for r in range(righe):
        for c in range(colonne):
            tabella[r][c] = 10 * int(r // 3 + 4 - abs((c - (colonne - 1) / 2) / 2))

    return tabella


def printTabella(tabella):
    for r in range(len(tabella)):
        for c in range(len(tabella[r])):
            print("%4s" % (tabella[r][c]), end="")
        print()


main()
