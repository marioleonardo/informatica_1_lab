import math

costo=100.35
TASSE=0.075

costoSpedizione=2.00
importo=math.trunc(((costo*(TASSE+1.00))+costoSpedizione)*100)/100
print(importo)