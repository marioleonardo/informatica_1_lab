import math
import random
import time

NUMERO_PALLINE_INIZIALI = 100
BOT_MODALITA_DIFFICILE = True

random.seed(time.time())
numeroPalline = random.randint(NUMERO_PALLINE_INIZIALI, math.ceil(NUMERO_PALLINE_INIZIALI * 1.5))
turnoPlayer = True


def estraiPalline(numeroPallineEstratte, numeroPalline):
    if (numeroPallineEstratte > 0 or numeroPalline == 1) and numeroPallineEstratte <= math.floor(numeroPalline / 2):

        if numeroPalline == 1:
            numeroPalline = 0
        else:
            numeroPalline = numeroPalline - numeroPallineEstratte
        return numeroPalline
    else:
        return -1


while (numeroPalline > 0):
    if turnoPlayer:

        turnoPlayer = False
        print(f"\nRimangono {numeroPalline} palline")
        numeroPallineTemporaneo = estraiPalline(int(input("Quante palline estrai?\n")), numeroPalline)

        if numeroPallineTemporaneo != -1:
            numeroPalline = numeroPallineTemporaneo
            print(f"\nRimangono {numeroPalline} palline")
        else:
            turnoPlayer = True

    else:
        turnoPlayer = True
        numeroPallinePrecedente = numeroPalline
        if BOT_MODALITA_DIFFICILE:
            numeroPallineTemporaneo = estraiPalline(math.ceil(numeroPalline / 2) - 1, numeroPalline)
        else:
            numeroPallineTemporaneo = estraiPalline(random.randint(1, math.floor(numeroPalline / 2)), numeroPalline)
        if numeroPallineTemporaneo != -1:
            numeroPalline = numeroPallineTemporaneo
            print(f"il bot ha estratto {numeroPallinePrecedente - numeroPalline} palline")
        else:
            turnoPlayer = False

if turnoPlayer:
    print("Ha vinto la macchina")
else:
    print("Ha vinto il player")
