def calcular(l):
    soma = 0
    for n in l:
        soma += n 
    comp = len(l)
    media = soma / comp
    return media

def avaliar(l):
    media = calcular(l)
    
    naMedia=[]
    acMedia=[]
    abMedia=[]

    for n in l:
        if n < media:
            abMedia.append(n)
        elif n > media:
            acMedia.append(n) 
        else:
            naMedia.append(n)
    return media, naMedia, abMedia, acMedia

def main():
    l=[]
    while True:
        nstr = input ("digite um número:")
        if nstr == "":
            break
        n = float (nstr)
        l.append(n)
    resposta = avaliar(l)
   
    print(resposta)
    print(f"A media é {resposta[0]}.")
    print(f"O número na média é {resposta[1]}.")
    print(f"O número abaixo da media é {resposta[2]}.")
    print(f"O número acima da media é {resposta[3]}.")

main()