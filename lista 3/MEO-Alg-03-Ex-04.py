quant_lados = int (input ("Quantos lados possui o polígino regular (entre 3 e 10)?"))

if quant_lados == 3:
    print (f"O nome do polígino regular de {quant_lados} é Triângulo.")
elif quant_lados == 4: 
   print (f"O nome do polígino regular de {quant_lados} é Quadrado.")
elif quant_lados == 5:
   print (f"O nome do polígino regular de {quant_lados} é Pentágono.")
elif quant_lados == 6:
   print (f"O nome do polígino regular de {quant_lados} é Hexágono.")
elif quant_lados == 7:
   print (f"O nome do polígino regular de {quant_lados} é Heptágono.")
elif quant_lados == 8:
   print (f"O nome do polígino regular de {quant_lados} é Octógono.")
elif quant_lados == 9:
   print (f"O nome do polígino regular de {quant_lados} é Eneágono.")
elif quant_lados == 10:
   print (f"O nome do polígino regular de {quant_lados} é Decágono.")
else:
   quant_lados < 3 or quant_lados > 10
   print ("A quantidade de lados está errada!")