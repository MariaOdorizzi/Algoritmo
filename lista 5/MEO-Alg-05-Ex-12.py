def main():
    senha = input ("Digite sua senha:")
    if verificar(senha):
        print (f"Sua senha {senha} é valida!")
    else:
        print(f"A senha {senha} é invalida!")

def verificar(senha):
    return caracter(senha) and maiuscula(senha) and minuscula(senha) and numero(senha)

def caracter(senha):
    if len(senha) >=8:
        return True
    return False

def maiuscula(senha):
    for i in senha:
        if i.isupper():
            return True
    return False

def minuscula(senha):
    for i in senha:
        if i.islower():
            return True
    return False

def numero(senha):
    for i in senha:
        if i.isdigit():
            return True
    return False

main ()