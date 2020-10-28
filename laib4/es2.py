stringa = input("Quale frase devo analizzare?\n")
maiuscole = ""
lettereAlternate = ""
underscore = ""
cifre = 0
posVocali = []

for index, i in enumerate(stringa, start=0):
    if i >= "A" and i <= "Z":
        maiuscole = maiuscole + i
    if index % 2 == 1:
        lettereAlternate = lettereAlternate + i
    if i in "aeiouAEIOU":
        underscore = underscore + "_"
        posVocali.append(index)
    else:
        underscore = underscore + i
    if i >= "0" and i <= "9":
        cifre = cifre + 1

print(maiuscole)
print(lettereAlternate)
print(underscore)
print(cifre)
print(posVocali)
