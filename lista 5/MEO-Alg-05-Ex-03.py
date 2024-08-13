def main():
    n = int (input ("Digite o número de itens adquiridos no pedido: "))
    r = calculo(n)
    print (f"O valor total do envio é R${r:.2f}.")

def calculo(n):
    resultado = 10.95 + (n - 1) * 2.95
    return resultado

main()