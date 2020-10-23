stato = input("Sei coniugato o no? (S/N) ")
stato = stato.upper()
stato = stato.startswith("S")

reddito = int(input("Qual è il tuo reddito imponibile? "))

if (not stato):
    if (reddito <= 8000):
        tassa = 0.10 * reddito
    elif (reddito <= 32000):
        tassa = 800 + 0.15 * reddito
    else:
        tassa = 4400 + 0.25 * reddito
else:
    if (reddito <= 16000):
        tassa = 0.10 * reddito
    elif (reddito <= 64000):
        tassa = 1600 + 0.15 * reddito
    else:
        tassa = 8800 + 0.25 * reddito

print(round(tassa, 2))
