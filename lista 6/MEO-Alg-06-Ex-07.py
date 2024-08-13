import random

def montarCartela():
    b = 'BINGO'
    i = 1
    f = 15
    d = {}
    for l in b:
        nA = random.sample(range (i, f), 5)
        d[l] = nA
        i += 15
        f += 15
    imprimirCartela(d)
    
def imprimirCartela(cartela):
    print ("------------------------------------------")
    print ("|   B","       I","      N","      G","      O   |",)
    print ("------------------------------------------")
    for x in range(5):
        print ("| ",cartela["B"][x],"\t",
            "| ",cartela["I"][x],"\t",
           "| ", cartela["N"][x],"\t",
           "| ", cartela["G"][x],"\t",
           "| ", cartela["O"][x],"\t","|",)
    print ("------------------------------------------")

montarCartela()