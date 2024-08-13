import math

n = float (input ("Quantos lados tem o polígono regular?"))
l = float ( input ("Qual é o comprimento de um lado do polígono regular?"))

area = n * l ** 2 / 4 * math. tan(math.pi / n)

print ("A área do polígono regular é ", area)