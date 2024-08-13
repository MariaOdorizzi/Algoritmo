def verificar(l):
    if len(l) == 1:
        return True
    ordem = sorted(l)
    if l == ordem:
        return True
    else:
        return False

def main():
    l1 = []
    while True:
        x = input ("Digite um item para inserir na lista (Para parar enter):")
        if x == "":
            break
        n = float(x)
        l1.append(n)
    print (verificar(l1))

main()