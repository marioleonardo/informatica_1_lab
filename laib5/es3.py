num = int(input("Qual è il numero?\n"))
fattori = []
finito = False

while not finito:
    for i in range(2, num + 1):
        if i == num:
            finito = True
            fattori.append(str(num))
        if num % i == 0 and not finito:
            num = int(num / i)
            fattori.append(str(i))
            break
            
print(", ".join(fattori))
