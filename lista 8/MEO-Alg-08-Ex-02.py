def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 :
        return 1 
    else:
       return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int (input ("Digite um número para fatorar:"))
    resposta = fibonacci(n)
    print (resposta)

main()