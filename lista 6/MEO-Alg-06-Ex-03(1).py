def remover(l, n):
    return l[n:-n]

def main():
    l = []
    while True:
        x = input ("Digite um número (Para parar enter):")
        if x == "":
            break
        nu = int(x)
        l.append(nu)
    if len(l) < 4:
        print ("Sua lista possui uma quantidade inferior a 4 objetos.")
    elif len(l) >= 4:
        n = int (input  ("Digite a quantidade de vezes que deseja remover o máximo e o mínimo da lista: "))
        print (remover(l, n))

main()