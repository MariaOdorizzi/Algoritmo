import random

def montarCartela():
    b = "BINGO"
    i = 1
    f = 15
    c = {}
    for l in b:
        nA = random.sample(range (i, f), 5)
        c[l] = nA
        i += 15
        f += 15
    return c
    
def sorteioCartela(c):
    s = random.sample(range(1, 75), 5)
    for nS in s:
        for valores in c.values():
            for x in range(len(valores)):
                if valores[x] == nS:
                    valores[x]= 0
    print (f"Os números sorteados são: {s}")
    return c

def verificarCartela(c):
    for li in c.values():
        if sum(li) == 0:
            return(True)
        
    for chave in c:
        if sum(c[chave]) == 0:
            return(True)
    
def imprimirCartela(c):
    print ("------------------------------------------")
    print ("|   B","       I","      N","      G","      O   |",)
    print ("------------------------------------------")
    for x in range(5):
        print ("| ",c["B"][x],"\t",
            "| ",c["I"][x],"\t",
           "| ", c["N"][x],"\t",
           "| ", c["G"][x],"\t",
           "| ", c["O"][x],"\t","|",)
    print ("------------------------------------------")

def main():
    imprimirCartela(sorteioCartela(montarCartela()))

main()