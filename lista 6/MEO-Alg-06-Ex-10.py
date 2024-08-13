def adicionar(l):
    strF = ""
    n = len(l)
    for i in l:
        if i != l[n - 2] and i != l[n-1]:
            strF = strF + i + ", "
        elif i == l[n - 2]:
            strF = strF + i + " e"
        elif i == l[n - 1]:
            strF = strF + " " + i
    return strF

def main():
    l1 = []
    while True:
        item = input ("Digite um item para inserir na lista (Para parar enter):")
        if item == "":
            break
        l1.append(item)
    final = adicionar(l1)
    print(final)

main()