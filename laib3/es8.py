start = input("unita di partenza? ").lower()
end = input("unita di arrivo? ").lower()
val = float(input("Qual è il valore? "))

options = {
    1: "ml",
    2: "l",
    3: "g",
    4: "kg",
    5: "mm",
    6: "m",
    7: "km",
}

volume = {
    1: 0.001,
    2: 1
}

peso = {
    3: 1,
    4: 1000
}

lunghezza = {
    5: 0.001,
    6: 1,
    7: 1000,
}

for numero, unita in options.items():
    if start == unita: start = numero
    if end == unita: end = numero

if (peso.get(start) and peso.get(end)):
    val = val * (peso.get(start) / peso.get(end))
elif (lunghezza.get(start) and lunghezza.get(end)):
    val = val * (lunghezza.get(start) / lunghezza.get(end))
elif (volume.get(start) and volume.get(end)):
    val = val * (volume.get(start) / volume.get(end))
else:
    exit(0)

print(val)
