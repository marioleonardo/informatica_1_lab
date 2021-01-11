N = 2
A = 4
B = 2


def main():
    print("Potenze del binomio (ax+by)^N")
    N, A, B = acquisisciDatiTastiera()
    tartaglia = generaTartaglia(N)
    coefficienti = generaCoefficienti(tartaglia, A, B)
    stringa = generaStringa(coefficienti)
    print(stringa)


def generaTartaglia(n):
    lista = [[1]]
    for indexRiga in range(n):
        listaTemp = [0] + lista[indexRiga] + [0]
        listaNew = []
        for indexColonna in range(indexRiga + 2):
            listaNew.append(listaTemp[indexColonna] + listaTemp[indexColonna + 1])
        lista.append(listaNew)
    lista.pop(0)
    return lista


def generaCoefficienti(tartaglia, A, B):
    risultato = []
    n = len(tartaglia[-1]) - 1
    for index in range(n + 1):
        risultato.append(tartaglia[-1][index] * (A ** (n - index)) * (B ** (index)))
    return risultato


def generaStringa(coefficienti):
    n = len(coefficienti)
    stringa = ""
    for index in range(n):
        stringa += f" {coefficienti[index]}"
        if (n - index - 1) != 0:
            stringa += f"x^{n - index - 1}"
        if index != 0:
            stringa += f"y^{index}"
        stringa += " +"
    stringa = stringa[:-1]
    return stringa


def acquisisciDatiTastiera():
    A = float(input("\nInserisci a: "))
    B = float(input("\nInserisci b: "))
    print("Calcolo le potenze(%.1fx + %.1fy)^N" % (A, B))
    N = int(input("\nInserisci N: "))
    return (N, A, B)


main()
