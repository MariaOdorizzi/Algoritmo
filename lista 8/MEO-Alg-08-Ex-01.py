def fatorial(n):
    if n >= 0:
        if n == 0 or n == 1:
            return 1
        else:
            f = 1
            i = 1
            while i <= n:
                f = f * i
                i += 1
            return f
    else:
        return "Número inválido"

def main():
    n = int(input("Digite um número para fatorar: "))
    f = fatorial(n)
    print(f)

main()