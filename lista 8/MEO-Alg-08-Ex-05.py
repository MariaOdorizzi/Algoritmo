def valores():
    n = input ("Digite um número:")
    if n != "":
        return float(n) + valores()
    else:
        return 0.0   

print (valores())