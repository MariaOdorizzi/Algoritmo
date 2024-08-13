while True:

    n = input ("Digite um número binário:")
    n0 = n [::-1]
    x = 1
    soma = 0

    for i in n0:
        i = int(i)
        if i == 1:
            soma += x
        x *= 2

    x = 1

    print(f"O número binário {n}, corresponde ao número decimal {soma}.")