pi = 3
n = 2
s = 1

for i in range (15):
    print (pi)
    pi = pi + (s * (4 / (n* (n + 1) * (n + 2))))
    s = -s
    n = n + 2