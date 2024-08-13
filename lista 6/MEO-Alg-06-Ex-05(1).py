l0 = []
l1 = []
l2 = []

while True:
    num = input ("Digite um número:")
    if num == "":
        break
    n = int (num)
    if n < 0:
        l1.append(n)
    elif n > 0:
        l2.append(n)
    elif n == 0:
        l0.append(n)
print (l1)
lF = l1 + l0 + l2
for i in lF:
    print (i)