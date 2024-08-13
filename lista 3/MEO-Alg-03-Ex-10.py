posicao  = str (input ("Digite uma posição do tabuleiro:"))

coluna = int (posicao [1:])
linha = posicao [:1]

if linha == "a":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa branca.")
    else:
        print (f"A posição {posicao} está em uma casa preta.")
elif linha == "b":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa preta.")
    else:
        print (f"A posição {posicao} está em uma casa branca.")
elif linha == "c":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa branca.")
    else:
        print (f"A posição {posicao} está em uma casa preta.")
elif linha == "d":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa preta.")
    else:
        print (f"A posição {posicao} está em uma casa branca.")
elif linha == "e":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa branca.")
    else:
        print (f"A posição {posicao} está em uma casa preta.")
elif linha == "f":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa preta.")
    else:
        print (f"A posição {posicao} está em uma casa branca.")
elif linha == "g":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa branca.")
    else:
        print (f"A posição {posicao} está em uma casa preta.")
elif linha == "h":
    if coluna % 2 == 0:
        print (f"A posição {posicao} está em uma casa preta.")
    else:
        print (f"A posição {posicao} está em uma casa branca.")