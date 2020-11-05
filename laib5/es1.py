stringhe = []
n = 0
stringa = input(f'Qual é la parola {n + 1}: ').lower().replace(" ", "")

while stringa != "":
    stringhe.append(stringa)
    n += 1
    stringa = input(f'Qual é la parola {n + 1}: ').lower().replace(" ", "")

for i in range(0, len(stringhe)):
    for j in range(0, len(stringhe) - i - 1):
        if stringhe[j] > stringhe[j + 1]:
            temp = ""
            temp = stringhe[j + 1]
            stringhe[j + 1] = stringhe[j]
            stringhe[j] = temp

print(stringhe)
