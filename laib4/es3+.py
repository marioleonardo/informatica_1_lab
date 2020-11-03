num = int(input("Inserisci 10 numeri\n"))
num = 0
numPrecedente = 0
N = 10
crescenza = True
i = 0

while i < N:
    if num < numPrecedente:
        crescenza = False
    i += 1
    numPrecedente = num
    num = int(input())

if crescenza:
    print("crescenti")
else:
    print("non crescenti")
