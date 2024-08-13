def main():
    frase = input ("Digite a frase para centralizar:")
    largura = int (input ("Digite a largura da linha:"))
    comprimento = len(frase)
    espaço = centralizar(comprimento, largura)
    print (espaço,frase)

def centralizar(comprmento, largura):
    calculo = largura - comprmento / 2
    s = " " * int (calculo)
    return s

main()