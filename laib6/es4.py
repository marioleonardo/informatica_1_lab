def main():
    figli = int(input("figli?\n"))
    reddito = int(input("reddito?\n"))
    while figli != -1 and reddito != -1:
        print(calcolaSussidio(reddito, figli))
        figli = int(input("figli?\n"))
        reddito = int(input("reddito?\n"))


def calcolaSussidio(reddito, figli):
    sussidio = 0
    if reddito < 20000:
        sussidio = 2000 * figli
    elif reddito < 30000:
        sussidio = 1500 * figli
    elif reddito < 40000:
        sussidio = 1000 * figli
    return sussidio


if __name__ == "__main__":
    main()
