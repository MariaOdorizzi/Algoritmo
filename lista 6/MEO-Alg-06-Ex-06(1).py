def lD(n):
    l = []
    i = 1
    while i <= n:
        if n % i == 0:
            l.append(i)
        i = i + 1
    return l

def main():
    n = int (input ("Digite o número inteiro:"))
    print (f"O número {n} possui como divisores:")
    for e in lD(n):
        print(e)

main()