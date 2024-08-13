x = int (input ("Digite um número:"))

r = x / 2

while ((r * r) - x) < 0.000000000001:
    r = (r + (x / r)) / 2

print (r)