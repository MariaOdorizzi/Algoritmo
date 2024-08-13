def retirarCaracteres(f):
    fScaracteres = ""
    for i in f:
        if i == "," or i == "." or i == "!" or i == " " or i == "?":
            continue
        else:
            fScaracteres = fScaracteres + i
    ffinal = fScaracteres.upper()
    return ffinal

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
    f1 = input ("Digite a 1º frase:")
    f2 = input ("Digite a 2º frase:")
    f1Final = retirarCaracteres(f1)
    f2Final = retirarCaracteres(f2)
    df1 = montagem(f1Final)
    df2 = montagem(f2Final)
    print (verificar(df1, df2))

main()