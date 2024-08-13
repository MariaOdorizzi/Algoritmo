import random

l = []

while len(l) < 6:
    n = random.randint(1, 60)
    if n not in l:
        l.append(n)
ordemCresc = sorted(l)
print (ordemCresc)
