n = int (input ("Digite o número inteiro:"))
fator = 2

if n < 2:
    print ("Erro: o número digitado é menor que 2!")

while fator <= n:
    if n % fator == 0:
        n = n / fator
        print (fator)
        continue
    if n % fator != 0:
        fator = fator + 1
    if fator % 2 == 0:
        fator = fator + 1