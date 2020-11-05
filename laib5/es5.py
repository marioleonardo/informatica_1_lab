import matplotlib.pyplot as plt

prede = 1000
predatori = 20
T = 160
predeCopulazione = 0.1
predatoriCopulazione = 0.01
predazione = 0.01
D = 0.00002
# predazioneAspettata = 1.5
# predazioneSuccesso = 0.18
predatoriT = []
predeT = []

for i in range(1, T + 1):
    # if predazioneAspettata * predatori <= int(prede * predazioneSuccesso):
    #     predazione = predazioneAspettata
    # else:
    #     predazione = round(prede * predazioneSuccesso / predatori)
    #
    # prede = int(prede + (predeCopulazione - 1) * prede - predazione * predatori)
    # predatori = predatori - int(predatori * ((1 - predazione / predazioneAspettata)))
    # predatori = predatori + int((predatoriCopulazione - 1) * predatori * predazione / predazioneAspettata)
    prede = prede * (1 + predeCopulazione - predazione * predatori)
    predatori = predatori * (1 - predatoriCopulazione + D * prede)

    predatoriT.append(predatori)
    predeT.append(prede)

plt.plot(range(1, T + 1), predatoriT, 'r--', range(1, T + 1), predeT, 'g^')
plt.show()
