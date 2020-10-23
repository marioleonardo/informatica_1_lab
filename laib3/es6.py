import math

num = float(input("Qual è il numero?\n"))
num = math.ceil(num)

if (num <= 4 and num >= 0):
    print("A" if num == 4 else "", end="")
    print("B" if num == 3 else "", end="")
    print("C" if num == 2 else "", end="")
    print("D" if num == 1 else "", end="")
    print("F" if num == 0 else "", end="")
