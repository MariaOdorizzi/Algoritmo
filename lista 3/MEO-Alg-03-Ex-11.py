import math

a = int (input ("Digite o valor de a:"))
b = int (input ("Digite o valor de b:"))
c = int (input ("Digite o valor de c:"))

z = b**2 - 4 * a * c

if z >= 0:
    x1 = (-(b)+ math.sqrt(z) )/(2 * a)
    x2 = (-(b)- math.sqrt(z) )/(2 * a)
    if z > 0:
        print (f"A função possui duas raízes e seus valores são {x1} e {x2}.")
    else:
        print (f"A função possui uma raíze e seu valor é {x1}")
else: 
    print ("A função não possui raízes reais.")