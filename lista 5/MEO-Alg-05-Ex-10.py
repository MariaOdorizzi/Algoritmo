def main():
    n = int (input ("Digite um numero:"))
    nprimo = verificar(n)
    if nprimo:
        print (f"O número {n} é primo!")
    else:
        print (f"O número {n} não é primo!")

def verificar(n):
    if n < 2:
        return False
    else:
        for i in range (2, n):
            if n % i == 0:
                 return False
        return True
                
main()