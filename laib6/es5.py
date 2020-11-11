def main():
    saldo = float(input("saldo?\n"))
    anni = int(input("anni?\n"))
    interesse = float(input("interesse?\n"))
    print(calcolaInteresse(saldo, anni, interesse))


def calcolaInteresse(saldo, anni, interesse):
    saldo = saldo * ((1 + interesse) ** anni)
    return round(saldo, 2)


if __name__ == "__main__":
    main()
