def main():
    x = float (input ("Digite o valor do comprimento do x: "))
    y = float (input ("Digite o valor do comprimento do y: "))
    p = pit(x, y)
    r2 = hip(p)
    print (f"a hipotenusa é {r2}")

def pit(x, y):
    r1 = (x ** 2) + (y ** 2)
    return r1

def hip(p):
    hip1 = p ** (1 / 2)
    return hip1

main()