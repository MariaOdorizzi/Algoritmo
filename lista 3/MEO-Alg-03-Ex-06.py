ladox = float (input ("Digite o valor do lado x:"))
ladoy = float (input ("Digite o valor do lado y:"))
ladoz = float (input ("Digite o valor do lado z:"))


if ladox > 0 and ladoy > 0 and ladoz > 0:
    if ladox == ladoy and ladoy == ladoz and ladox == ladoz:
        print ("O triângulo é equilátero.")
    elif ladox != ladoy and ladoy != ladoz and ladox != ladoz:
        print ("O triângulo é escaleno.")
    else:
        print ("O triângulo é isósceles")
else:
    print ("Os valores incorretos")