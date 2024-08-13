import math

l1 = float (input ("Qual é o comprimento do 1º lado do triângulo?"))
l2 = float (input ("Qual é o comprimento do 2º lado do triângulo?"))
l3 = float (input ("Qual é o comprimento do 3º lado do triângulo?"))

l = (l1 + l2 + l3) / 2

area = math.sqrt(l * (l - l1) * (l - l2) * (l - l3))

print ("A área do triângulo é ", area)