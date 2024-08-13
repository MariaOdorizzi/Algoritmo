def main():
    string = input ("Digite alga coisa:")
    resultado = isInteger(string)
    if resultado == True:
        print ("A string é um inteiro.")
    else:
        print ("A string não é um inteiro.")

def isInteger(string):
    string = string.strip()
    for i in string:
        if i == "+" or i == "-":
            continue
        i = ord(i)
        if i >= 48 and i < 58:
            return True
        else:
            return False

main()