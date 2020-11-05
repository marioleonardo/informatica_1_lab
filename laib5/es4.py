import time

import matplotlib.pyplot as plt

a = 32311
m = 2 ** 22
b = 1729

seed = int(time.time() * 10)
old = seed
n1 = int(input("Inserisci numero 1: "))
n2 = int(input("Inserisci numero 2: "))
n3 = int(input("Inserisci numero numeri: "))
plot = int(input("Plot? "))
x = []

for i in range(1, n3 + 1):
    new = ((a * old + b) % m) % (abs(n2 - n1) + 1) + min(n1, n2)
    old = round(((a * old + b) % m), 10)
    if not plot:
        print(new)
    else:
        x.append(new)

if plot:
    plt.hist(x, density=True, bins=(abs(n2 - n1) + 1))
plt.show()
