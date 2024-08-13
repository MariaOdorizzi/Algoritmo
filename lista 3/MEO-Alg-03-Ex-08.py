nota = str (input ("Digite uma nota musical (escola anglo-saxônica):"))

letra = nota [:1]
oitava = int (nota [1:])
frequencia = 0

if letra.lower() == "c":
    frequencia = 261.63 / (2 ** (4 - oitava))
elif letra.lower() == "d":
    frequencia = 293.66 / (2 ** (4 - oitava))
elif letra.lower() == "e":
     frequencia = 329.63 / (2 ** (4 - oitava)) 
elif letra.lower() == "f":
    frequencia = 349.23 / (2 ** (4 - oitava)) 
elif letra.lower() == "g":
    frequencia = 392.00 / (2 ** (4 - oitava)) 
elif letra.lower() == "a":
     frequencia = 440.00 / (2 ** (4 - oitava)) 
elif letra.lower() == "b":
     frequencia = 493.88 / (2 ** (4 - oitava)) 
else:
   print ("A nota musical está incorreta!")

print (f"A frequência da nota {nota} é de {frequencia}")