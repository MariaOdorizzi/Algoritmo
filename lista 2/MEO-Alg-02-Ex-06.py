num = int (input ("Digite um número com quatro dígitos: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

soma = u + d + c + m

print (f"A soma dos quatro dígitos do nuémero {num} é igual a {soma}.")