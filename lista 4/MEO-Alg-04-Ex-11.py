while True:
    frase = input ("Digite a frase ou palavra (para parar enter):")
    if frase == "":
        break
    frase = ''.join(frase.split())
    n = len(frase)
    palindromo = True
    for i in range (n):
        if frase[i] != frase[n-1-i]:
            palindromo = False
            break

    if palindromo == True:
        print (f"A frase/palavra, {frase}, é palíndroma.")
    else:
        print (f"A frase/palavra, {frase}, não é palíndroma.")