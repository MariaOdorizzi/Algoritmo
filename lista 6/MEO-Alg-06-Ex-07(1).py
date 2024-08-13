def lD(num):
    l = []
    i = 1
    while i < num:
        if num % i == 0:
            l.append(i)
        i = i + 1
    return l

def numP(n):
    soma = 0
    divisor = lD(n)
    for num in divisor:
        soma = soma + num
    if soma == n:
        return True
    else:
        return False

def main():
    for i in range(1, 10000):
        if numP(i):
            print (i)

main()