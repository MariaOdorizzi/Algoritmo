troco = int (input ("Informe o valor do troco (centavos):"))

moeda_50 = troco // 50
troco = troco % 50

moeda_25 = troco // 25
troco = troco % 25

moeda_10 = troco // 10
troco = troco % 10

moeda_5 = troco // 5
troco = troco % 5

moeda_1 = troco

print (f"Quantidade de moedas de 50 centavos: {moeda_50}")
print (f"Quantidade de moedas de 25 centavos: {moeda_25}")
print (f"Quantidade de moedas de 10 centavos: {moeda_10}")
print (f"Quantidade de moedas de 5 centavos: {moeda_5}")
print (f"Quantidade de moedas de 1 centavos: {moeda_1}")