def main():
    while True:
        numeroRomano = (input("numero romano?\n"))
        print(calcolaArabo(numeroRomano))


def calcolaArabo(numeroRomano):
    numeroRomano = numeroRomano.upper()
    oldNum = 2000
    risultato = 0
    frequenzaOldNum = 1
    for index, char in enumerate(numeroRomano):
        if char == "I":
            num = 1
        if char == "V":
            num = 5
        if char == "X":
            num = 10
        if char == "L":
            num = 50
        if char == "C":
            num = 100
        if char == "D":
            num = 500
        if char == "M":
            num = 1000

        if num <= oldNum:
            risultato = risultato + num
            if num == oldNum:
                frequenzaOldNum = frequenzaOldNum + 1
            else:
                frequenzaOldNum = 1
            oldNum = num
        else:

            risultato = risultato - (2 * oldNum * frequenzaOldNum)
            risultato = risultato + num

    return risultato


if __name__ == "__main__":
    main()
