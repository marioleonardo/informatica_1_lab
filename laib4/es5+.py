n = int(input("LATO?\n"))
i = 0

while i < n ** 2:
    if (i) % n + 1 <= (i + n) // n:

        print("*", end="")
    else:
        print(" ", end="")

    if (i + 1) % n == 0:
        print("")

    i = i + 1
