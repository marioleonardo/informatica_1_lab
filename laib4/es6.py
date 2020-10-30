stringa = input("Qual é la stringa?\n")

for i in range(1, len(stringa)):
    for j in range(0, len(stringa)):
        if j + i <= len(stringa):
            print(stringa[j:j + i])
