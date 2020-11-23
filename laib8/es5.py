import random as rd
import time

rd.seed(time.time())


def main():
    lista = [rd.randint(0, 100) for i in range(20)]
    print(lista)
    lista.sort()
    print(lista)


if __name__ == "__main__":
    main()
