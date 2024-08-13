def precedencia(x):
    if x == "+" or x == "-":
        return 1
    elif x == "*" or x == "/":
        return 2
    elif x == "^":
        return 3
    else:
        return -1

def main():
    oper = input ("Digite o operador:")
    resposta = precedencia(oper)
    if resposta >= 1:
        print (resposta)
    else:
        print ("Erro: não foi inserido um operador.")

main()