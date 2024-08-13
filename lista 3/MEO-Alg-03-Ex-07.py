nivel = float (input ("Digite o valor do nível do volume em decibéis:"))

if nivel < 40:
    print ("O nível do volume está abaixo do nível de volume de uma sala silenciosa.")
elif nivel == 40:
    print ("O nível do volume equivale ao volume de uma sala silenciosa.")
elif nivel > 40 and nivel < 70:
    print ("O nível do volume está entre o nível do volume de uma sala silenciosa com um desperatdor.")
elif nivel == 70:
    print ("O nível do volume equivale ao volume de um despertador.")
elif nivel > 70 and nivel < 106:
    print ("O nível do volume está entre o nível do volume de um desperatdor com um cortador de grama.")
elif nivel == 106:
    print ("O nível do volume equivale ao volume de um cortador de grama.")
elif nivel > 106 and nivel < 130:
    print ("O nível do volume está entre o nível do volume de um cortador de grama com uma britadeira.")
elif nivel == 130:
    print ("O nível do volume equivale ao volume de uma britadeira.")
elif nivel > 130:
    print ("O nível do volume está acima do nível de volume de uma britadeira.")