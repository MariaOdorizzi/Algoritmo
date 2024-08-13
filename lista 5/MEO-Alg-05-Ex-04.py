def main():
    a = float (input ("Digite um número: "))
    b = float (input ("Digite um número: "))
    c = float (input ("Digite um número: "))
    resultado = calculo(a,b,c)
    print (f"A mediana dos números inseridos é {resultado}.")

def calculo(a,b,c):
    max = max(a,b,c)
    min = min(a,b,c)
    mediana = (a + b + c) - min - max
    return mediana

main()