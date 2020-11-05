bigliettiDisponibili = 100
MAX = 4
clienti = 0

while bigliettiDisponibili > 0:
    bigliettiAcquistati = int(input("Biglietti? "))
    if bigliettiAcquistati > 4 or bigliettiAcquistati > bigliettiDisponibili:
        print("riprova")
    else:
        clienti += 1
        print(f"ecco {bigliettiAcquistati} biglietti")
        bigliettiDisponibili -= bigliettiAcquistati
        print(bigliettiDisponibili)

print(f"biglietti finiti, clienti {clienti}")
