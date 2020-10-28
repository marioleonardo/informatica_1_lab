num = 0
numeri = []
numeriDuplicati = []
max = -1
min = -1
numeriPari = 0
numeriDispari = 0
numeriSomma = 0

while (num >= 0):
    num = int(input("Qual é il numero?\n"))
    if num >= 0:
        if num > max:
            max = num
        if num < min or min == -1:
            min = num
        if num % 2 == 0:
            numeriPari = numeriPari + 1
        else:
            numeriDispari = numeriDispari + 1
        numeriSomma = numeriSomma + num
        if ((num in numeri) and (num not in numeriDuplicati)):
            numeriDuplicati.append(num)
        numeriDuplicati.sort()
        numeri.append(num)

        print(f"il massimo é {max} e il minimo é {min}")
        print(f"Ci sono {numeriPari} numeri pari e {numeriDispari} numeri dispari")
        print(f"La somma dei numeri inseriti é {numeriSomma}")
        print(f"I valori duplicati sono {numeriDuplicati}\n")
