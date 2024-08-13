n = int (input ("Digite o valor de N:"))

a = 0

if n > 0:
    for e in range (n, 0, -1):
        a += e / (n - e + 1 )
    print (f"O valor de A é {a}")
else:
    print ("Número inválido! Por favor, insira um número inteiro positivo.")