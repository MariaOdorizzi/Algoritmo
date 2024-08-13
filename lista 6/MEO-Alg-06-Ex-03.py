def buscaReversa(d1,n):
    l = []
    for x, y in d1.items():
        if y == n:
            l.append(x)
    return(l)

def main():
    d1 = {}
    while True:
        chave = input ("Digite uma chave (Para parar enter):")
        if chave == "":
            break
        v = input ("Digite o número da chave:")
        d1[chave] = v
    n = input ("Digite o número da chave que deseja buscar:")
    resultado = buscaReversa(d1, n)
    print (resultado)

main()