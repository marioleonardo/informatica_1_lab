nome=input()
nomeNuovo=''

for i in range(3):
    nomeNuovo=nomeNuovo+nome[i]

nomeNuovo=nomeNuovo+"..."

for i in range(3):
    nomeNuovo=nomeNuovo+nome[(len(nome)-1)-(2-i)]

print(nomeNuovo)