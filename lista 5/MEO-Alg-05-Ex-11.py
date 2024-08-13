import random

def main():
    x = random.randint(7,10)
    senha = ""
    senhaf = criar(x, senha)
    print(f"Senha é: {senhaf}")

def criar(x, senha):
    for numero in range(x):
        ascii = random.randint(33,126)
        caracter = chr(ascii)
        senha = senha + caracter
    return senha

main()