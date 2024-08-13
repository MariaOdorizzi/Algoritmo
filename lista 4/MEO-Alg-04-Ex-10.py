while True:
    palavra = input ("Digite a palavra (para parar enter):")
    if palavra == "":
        break
    n = len(palavra)
    palindromo = True
    for i in range(n):
        if palavra[i] != palavra[n - 1 - i]:
            palindromo = False
            break
    
    if palindromo == True:
        print (f"A palavra {palavra} é palíndroma.")
    else:
        print (f"A palavra {palavra} não é palíndroma.")