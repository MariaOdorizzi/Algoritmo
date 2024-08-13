def main():
    x = int (input ("Digite um número:"))
    resposta = ordinal(x)
    print (resposta)

def ordinal(x):
    if x == 1:
        return "Primeiro"
    elif x == 2:
        return "Segundo"
    elif x == 3:
        return "Terceiro"
    elif x == 4:
        return "Quarto"
    elif x == 5:
        return "Quinto"
    elif x == 6:
        return "Sexto"
    elif x == 7:
        return "Sétimo"
    elif x == 8:
        return "Oitavo"
    elif x == 9:
        return "Nono"
    elif x == 10:
        return "Décimo"
    elif x == 11:
        return "Décimo primeiro"
    elif x == 12:
        return "Décimo segundo"
    elif x > 12 or x < 1:
        return ""

main()