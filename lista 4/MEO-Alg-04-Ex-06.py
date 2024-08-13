while True:
    g = input ("Digite o grupo de 8 bits (para parar enter):")
    if g == "":
        break
    if len(g) != 8:
        print ("Erro: a palavra precisa ter 8 bits!")
        continue
    if g.count("1") + g.count("0") != 8:
         print ("ERRO: o grupo precisa conter apenas 0 ou 1!")
         continue
    if g.count("1") % 2 == 0:
          print ("O bit de pariedade precisa ser 1")
    else:
            print ("O bit de pariedade precisa ser 0")
print ("Acabou")