def verificar(f):
    l1 = f.split()
    l2 = []
    for i in l1:
        nP = ""
        for c in i:
            if c.isalpha():
                nP = nP + c
        l2.append(nP)
    return l2

def main():
    f = input ("Digite uma frase:")
    resultado = verificar(f)
    print (resultado)

main()