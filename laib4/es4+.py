n = int(input("LATO?\n"))
i = 0

while i < n ** 2:
    if i < n or i >= n * (n - 1) or (i + 1) % n == 1 or (i + 1) % n == 0:

        print("*", end="")
    else:
        print(" ", end="")

    if (i + 1) % n == 0:
        print("")

    i = i + 1
