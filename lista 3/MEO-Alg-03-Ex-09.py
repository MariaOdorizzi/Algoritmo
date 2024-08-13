mes = str (input ("Digite o mês:"))
dia = int (input ("Digite o dia:"))

if  mes.lower() == 'janeiro':
    if dia == 1:
        print (f"Na data {dia} de {mes} tem o feriado de Confraternização universal.")
elif mes.lower() == 'abril':
    if dia == 21:
        print (f"Na data {dia} de {mes} tem o feriado de Tiradentes.")
elif mes.lower() == 'maio':
    if dia == 1:
        print (f"Na data {dia} de {mes} tem o feriado do Dia do trabalho.")
elif mes.lower() == 'setembro':
    if dia == 7:
        print (f"Na data {dia} de {mes} tem o feriado de Independência do Brasil.")
elif mes.lower() == 'outubro':
    if dia == 12:
        print (f"Na data {dia} de {mes} tem o feriado de Nossa Senhora Aparecida.")
elif mes.lower() == 'novembro':
    if dia == 2:
        print (f"Na data {dia} de {mes} tem o feriado de Finados.")
    elif dia == 15:
        print (f"Na data {dia} de {mes} tem o feriado da Proclamação da República.")
elif mes.lower() == 'dezembro':
    if dia == 25:
        print (f"Na data {dia} de {mes} tem o feriado de Natal.")
else:
    print ("O mês e/ou o dia informados não correspondem a um feriado nacional.")