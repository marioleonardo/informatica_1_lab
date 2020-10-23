import math

lato1=int(input())
lato2=int(input())

area=lato1*lato2
perimetro=lato1*2+lato2*2
diagonale=math.sqrt(lato1**2+lato2**2)
print(area)
print(perimetro)
print(diagonale)