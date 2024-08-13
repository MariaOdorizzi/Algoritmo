def main():
    vi = 4
    m = converçao()
    vt = calculo(vi, m)
    print (f"O valor final da corrida é R$ {vt:.2f}.")

def converçao():
    q = float (input ("Digite quantos quilometros foram percorridos:"))
    v = (q * 1000)
    return v

def calculo(vi, m):
    resultado = vi + ((m / 140) * 0.25)
    return resultado

main()