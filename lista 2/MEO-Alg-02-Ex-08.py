num = int (input ("Digite um número com três dígitos: "))

c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

soma = (c + (d * 10) + (u * 100))
 
print (f"O nuúmero dado {num}, trocando a ordem obtendo {soma}")