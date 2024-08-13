dia = int (input ("Digite o número de dias:"))
horas = int (input ("Digite o número de horas:"))
minutos = int (input ("Digite o número de minutos:"))
segundos = int (input ("Digite o número de segundos:"))

total = (dia * 86400 )+ (horas * 3600) + (minutos * 60) + segundos

print ("A quantidade total deste intervalo de tempo informado é", total,"segundos.")