def diferenca(c1, c2):
    u = c1.union(c2)
    i = c1.intersection(c2)
    return u.difference(i)

def main():
    con1 = set()
    con2 = set()
    while True:
        n = input ("Digite um número do 1ºconjunto (Para parar enter)")
        if n == "":
            break
        n = int(n)
        con1.add(n)
    while True:
        a = input ("Digite um número do 2ºconjunto (Para parar enter)")
        if a == "":
            break
        a = int(a)
        con2.add(a)
    print (diferenca(con1, con2))

main()