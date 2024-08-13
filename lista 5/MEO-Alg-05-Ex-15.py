def main():
    string = input ("Digite um único digito hexadecimal ou um número inteiro (0 a 15):")
    if len(string) == 2:
        resposta = int2hex(string)
        print (f"A converção do número inteiro para o digito hexadecimal é {resposta}.")
    else:
        resposta = hex2int(string)
        print (f"A converção do digito hexadecimal para o número inteiro é {resposta}.")

def int2hex(string):
    if (string == "0"
        or string == "1"
        or string == "2"
        or string == "3"
        or string == "4"
        or string == "5"
        or string == "6"
        or string == "7"
        or string == "8"
        or string == "9"
    ):
        return string
    if string == "10":
        return "A"
    elif string == "11":
        return "B"
    elif string == "12":
        return "C"
    elif string == "13":
        return "D"
    elif string == "14":
        return "E"
    elif string == "15":
        return "F"

def hex2int(string):
    if string == "A" or string == "a":
        return 10
    elif string == "B" or string == "b":
        return 11
    elif string == "C" or string == "c":
        return 12
    elif string == "D" or string == "d":
        return 13
    elif string == "E" or string == "e":
        return 14
    elif string == "F" or string == "f":
        return 15
    elif (string == "0"
        or string == "1"
        or string == "2"
        or string == "3"
        or string == "4"
        or string == "5"
        or string == "6"
        or string == "7"
        or string == "8"
        or string == "9"
    ):
        return string

main()