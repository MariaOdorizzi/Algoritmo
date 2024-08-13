import math

r = float (input ("Qual o valor do raio?"))

area = math.pi * r ** 2

volume = 4 / 3 * math.pi * r

print ("A área do círculo de raio {} é igual {}". format(r, area))
print ("O volume da esfera de raio {} é igual {}". format(r, volume))