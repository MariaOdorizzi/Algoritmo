def main():
    f1 = input ("Digite a frase:")
    x = verificar(f1)
    print (f"A frase corrigida é {x}" )

def verificar(f1):
    f2 = ""
    for i in range (len(f1)):
        if i == 0:
            f2 = (f2 + f1[i].upper())
        elif i == 1:
            f2 = f2 + f1[i]
        else:
            lant1 = f1[i - 1]
            lant2 = f1[i - 2]
            if lant1 == " " and (lant2 == "!" or lant2 == "." or lant2 == "?"):
                f2 = f2 + f1[i].upper()
            else:
                f2 = f2 + f1[i]
    return f2

main()