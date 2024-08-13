valor = 0

while True:
    resposta = input ("Digite a idade:")
    if resposta == "":
        break
    idade = int (resposta)
    if idade <= 2:
        valor = valor
    if idade <= 12 and idade > 2:
        valor = valor + 14
    if idade > 13 and idade < 65:
        valor = valor + 23
    if idade >= 65:
        valor = valor + 18

print (f"O preço total das entradas é R$ {valor:.2f}")