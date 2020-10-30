n = int(input("Qual é il numero?\n"))
print("\n")
i = 0

while (i < n):
    print(n * "*")
    i = i + 1

i = 0
print()

while (i < 2 * n - 1):
    print(((abs(n - (i + 1))) * " ") + (((n - 1 - (abs(n - (i + 1)))) * 2 + 1) * "*") + (((abs(n - (i + 1))) * " ")))
    i = i + 1
