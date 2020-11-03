r = int(input("Quale raggio?\n"))
d = 2 * r

for y in range(-r, r + 1):
    for x in range(-r, r + 1):
        if ((x / r) ** 2 + (y / r) ** 2 <= 1.03):
            print("*  ", end="")
        else:
            print("   ", end="")
    print("")
