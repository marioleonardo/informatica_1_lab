sommaNumeri = 0
numeri = ""

while sommaNumeri < 21:
    i = input("Quale numero?\n")
    numeri = numeri + i
    i = int(i)
    sommaNumeri = sommaNumeri + i

print(sommaNumeri)
print(numeri)
