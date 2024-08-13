n = int (input ("Digite o valor de N:"))

a = 0

if n > 0:
    for e in range (1, n + 1):
        a += 1 / e
    print (f"O valor de A é {a}")
else:
    print ("Número inválido! Por favor, insira um número inteiro positivo.")