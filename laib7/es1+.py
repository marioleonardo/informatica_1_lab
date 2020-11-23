numeri = input("numeri?\n") + " "
numeroFlag = False
numeroStringa = ""
quadrati = ""

for char in numeri:
    if char in "1234567890":
        numeroFlag = True
        numeroStringa = numeroStringa + char
    else:
        numeroFlag = False
        if numeroStringa != "":
            numero = int(numeroStringa)
            quadrato = numero ** 2
            quadrati = quadrati + str(quadrato) + " "
        numeroStringa = ""

print(quadrati)
