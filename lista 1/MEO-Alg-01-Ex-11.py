import math

lon1 = float (input (" Digite a longitude do ponto A:"))
lat1 = float (input (" Digite a latitude ponto A:"))
lon2 = float (input (" Digite a longitude do ponto B:"))
lat2 = float (input (" Digite a latitude ponto B:"))

lon1_rad = math.radians (lon1)
lat1_rad = math.radians (lat1)
lon2_rad = math.radians (lon2)
lat2_rad = math.radians (lat2)

distancia = 6371.01 * math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(lon1_rad - lon2_rad))

print ("A distância entre os pontos A e b em quilômetros ao longo da superfície", distancia, "km²")