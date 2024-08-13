x = float (input ("Digite a coordenada x de um ponto:"))
y = float (input ("Digite a coordenada y de um ponto:"))
perimetro = 0
x0 = x
y0 = y

while True:
    resposta = input ("Digite a coordenada x de um ponto (para parar enter):")
    if resposta == "":
        break
    yat = float (input ("Digite a coordenada y de um ponto:"))
    xat = float (resposta)
    d = (((xat - x) ** 2) + ((yat - y) ** 2)) ** 0.5
    perimetro = perimetro + d
    x = xat
    y = yat

d = (((x0 - x) ** 2) + ((y0 - y) ** 2)) ** 0.5
perimetro = perimetro + d
print (f"O perímetro desse polígono é {perimetro}")