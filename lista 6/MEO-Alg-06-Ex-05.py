def montagem(p):
    d = {}
    for i in p:
        if (i in d) == True:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d

def verificar(d1, d2):
    c1 = set(d1.keys())
    c2 = set(d2.keys())
    if c1 != c2:
        return False
    for chave in d1:
        if d1[chave] != d2[chave]:
            return False
    return True

def main():
    p1 = input ("Digite a 1º palavra: ")
    p2 = input ("Digite a 2º palavra: ")
    dA = montagem(p1)
    dB = montagem(p2)
    print (dA, len(dA))
    print (dB, len(dB))
    print (verificar(dA, dB))

main()