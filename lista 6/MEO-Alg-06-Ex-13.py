def countRange(l, max, min):
    q = 0
    for i in l:
        if i >= min and i < max:
            q = q + 1
    return q

def main():
    l1 = []
    while True:
        x = input ("Digite um item para inserir na lista (Para parar enter):")
        if x == "":
            break
        n = float (x)
        l1.append(n)
    max = float (input ("Digite um valor máximo:"))
    min = float (input ("Digite um valor mínimo:"))
    print (countRange(l1, max, min))

main()