l1 = []
l2 = []

while True:
    p = input ("Digite a palavra:")
    if p == "":
        break
    l1.append(p)
for i in l1:
    if l2.count(i) == 0:
        l2.append(i)
print (l2)