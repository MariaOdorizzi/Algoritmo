l = []
while True:
    n = int (input ("Digite um número (Para parar digite 0):"))
    if n == 0:
        break
    l.append(n)
ordemD = sorted(l, reverse = True)
print (ordemD)