num = int (input ("Digite um número com três dígitos: "))

c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print (f"O nuúmero dado {num}, sendo separado é {c} centena, {d} dezenas e {u} unidades")