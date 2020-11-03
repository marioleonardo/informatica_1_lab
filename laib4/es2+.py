num = int(input("Inserisci 10 numeri\n"))
i = 0

while i < 10:
    if num < 0:
        print("numeri non positivi")
        exit()
    i += 1
    num = int(input())

print("numeri positivi")
