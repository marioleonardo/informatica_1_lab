import math

num = input("Qual é il numero?\n")

a = math.floor(len(num) / 2)

for i in range(a):
    if (num[i] != num[len(num) - 1 - i]):
        exit(0)

print("palindromo")
