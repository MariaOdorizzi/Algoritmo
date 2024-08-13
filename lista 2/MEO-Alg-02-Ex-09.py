data = (input ("Digite a data (DDMMAA):"))

D = data [:2]
M = data [2:4]
A = data [4:]

data_in = A + M + D

print (f"A data impressa invertida {data_in}")