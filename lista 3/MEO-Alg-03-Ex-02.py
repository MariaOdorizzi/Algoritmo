idade_cao = int (input ("Qual a idade do cachorro?"))

if idade_cao > 2:
    idade_canina = 21
    idade_cao = idade_cao - 2
    idade_canina = idade_canina + (idade_cao * 7)
    print (f"A idade do cachorro é {idade_canina} anos")
elif idade_cao < 0:
    print ("Idade inexistente")
else:
    idade_canina = idade_cao * 10.5
    print (f"A idade do cachorro é {idade_canina} anos")