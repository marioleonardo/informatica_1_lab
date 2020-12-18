def main():
    N = 300000
    numeri = {2}
    n = 3
    while n <= N:
        numeri.add(n)
        n += 1

    nextNumberToDeleteMultipliers = min(numeri)
    numberToFinishDeleting = int(N ** 1 / 2)
    while nextNumberToDeleteMultipliers <= numberToFinishDeleting:
        index = nextNumberToDeleteMultipliers * 2
        while index <= N + 1:
            if index in numeri:
                numeri.discard(index)
            index += nextNumberToDeleteMultipliers
        nextNumberToDeleteMultipliers += 1

    file = open("es4output.txt", "w")
    i = 0
    for n in numeri:
        file.write(str(n) + "  ")
        i += 1
        if i % 15 == 0:
            file.write("\n")
    file.close()


main()
