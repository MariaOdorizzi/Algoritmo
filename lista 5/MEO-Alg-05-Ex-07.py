def main():
    c1 = float (input ("Digite o comprimento do 1º canudo:"))
    c2 = float (input ("Digite o comprimento do 2º canudo:"))
    c3 = float (input ("Digite o comprimento do 3º canudo:"))
    
    if verif1(c1,c2,c3) <= c1:
        print ("Não é possível formar um triângulo.")
    elif verif2(c1,c2,c3) <= c2:
        print ("Não é possível formar um triângulo.")
    elif verif3(c1,c2,c3) <= c3:
        print ("Não é possível formar um triângulo.")
    else:
        print ("É possível formar um triângulo.")

def verif1(c1,c2,c3):
    v1 = c2 + c3
    return v1

def verif2(c1,c2,c3):
    v2 = c1 + c3
    return v2

def verif3(c1,c2,c3):
    v3 = c1 + c2
    return v3

main()