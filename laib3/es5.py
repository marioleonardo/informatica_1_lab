anno=int(input("qual è l'anno?\n"))

if((anno>1587 and (anno%400!=0 and anno%100==0)) or anno%4!=0):
    print("anno non bisestile")
else:
    print("anno bisestile")
