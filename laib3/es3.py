while (True):
    word = input("dimmi la password: ")
    numeroLettere = 0
    numeroCifre = 0

    for i in word:
        if (i <= "Z" and i >= "A" or i >= "a" and i <= "z"):
            numeroLettere = numeroLettere + 1
        elif (i >= "0" and i <= "9"):
            numeroCifre = numeroCifre + 1

    if (word[0] >= "A" and word[0] <= "Z"):
        print("inizia con la maiuscola")

    if (word.endswith(".")):
        print("finisce con  il punto")

    elif (numeroLettere == len(word)):
        print("contiene soltanto lettere")
        if (word.lower() == word):
            print("contiene soltanto lettere minuscole")
        elif (word.upper() == word):
            print("contiene soltanto lettere maiuscole")

    elif (numeroCifre == len(word)):
        print("contiene soltanto cifre")

    elif (numeroCifre + numeroLettere == len(word)):
        print("contiene soltanto lettere e cifre")

    print("")
