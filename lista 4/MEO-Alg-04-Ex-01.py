l = []

while True:
    n = float (input ("Digite um número (para encerrar digite 0):"))
    if n == 0:
        break
    l.append(n)

if len(l) == 0:
    print ("Erro: O primeiro valor não pode ser 0.")

x = 0

while x < len(l):
    print (f"{x+1}º número = {l[x]}")
    x += 1

soma = 0

for e in l:
    soma += e
print (f"A média é: {soma / len(l)}.")