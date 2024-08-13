def main():
    numero = input ("Digite um número:")
    baseI = int (input ("Digite qual a base do seu número:"))
    baseC = int (input ("Digite a base para a conversão:"))
    print (f"Seu número convertido é {converteB(numero, baseI, baseC)} na base {baseC}.")

def int2hex(n):
    if 0 <= n <= 9:
        return str(n)
    elif n == 10:
        return "A"
    elif n == 11:
        return "B"
    elif n == 12:
        return "C"
    elif n == 13:
        return "D"
    elif n == 14:
        return "E"
    elif n == 15:
        return "F"

def hex2int(string):
    if string.isdigit():
        return int(string)
    else:
        string = string.upper()
        if string == "A":
            return 10
        elif string == "B":
            return 11
        elif string == "C":
            return 12
        elif string == "D":
            return 13
        elif string == "E":
            return 14
        elif string == "F":
            return 15

def converter(numero, base):
    dec = 0
    n = len(numero)
    expoente = n - 1
    for i in range(n):
        dec = dec + hex2int(numero[i]) * base ** expoente
        expoente = expoente - 1
    return dec

def dec2base(numeroD, base):
    resultado = ""
    while numeroD > 0:
        resto = numeroD % base
        resultado = int2hex(resto) + resultado
        numeroD = numeroD // base
    return resultado

def converteB(numero, baseI, baseD):
    decimal = converter(numero, baseI)
    resultado = dec2base(decimal, baseD)
    return resultado

main()