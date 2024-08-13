n = int (input ("Digite o número em decimal:"))
x = 0
soma = 0
d = n

while n != 0:
    r = n % 2
    soma += r * (10 ** x)
    x += 1
    n = n // 2
print (f"A conversão do número decimal {d} para binário é {soma}")