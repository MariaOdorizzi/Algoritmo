vi = 4.95

print ("Preço\t\tDesconto\t\tPreço com desconto")

while vi < 25:
    desconto = 60
    print (f"R${vi:.2f}\t\t{desconto}%\t\t\tR${(vi * 0.6):.2f}")
    vi = vi + 5