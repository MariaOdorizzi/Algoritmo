seg_t = int (input ("Digite a quantidade de segundos:"))

dias = seg_t // 86400
seg_r = seg_t % 86400

horas = seg_r // 3600
seg_r = seg_r % 3600

minutos = seg_r // 60
seg_r = seg_r % 60

segundos = seg_r

print ("A quantidade de segundos convertidos em dias:", dias, ", em horas:", horas, ", em minutos:", minutos, "e em segundos:", segundos, "." )