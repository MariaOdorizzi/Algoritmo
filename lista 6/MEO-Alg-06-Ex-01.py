def verificar(c1):
    c2 = set(c1)
    if len(c2) == len(c1):
        return True
    else:
        return False

def main():
    f = input ("Digite uma frase:")
    str1 = list(f)
    print (verificar(str1))

main()