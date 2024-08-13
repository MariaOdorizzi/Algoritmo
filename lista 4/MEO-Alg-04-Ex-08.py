msg = input ("Digite a frase que deseja codificar:")
d = int (input ("Digite a distância de deslocamento das letras:"))
msg1 = ""

for l in msg: 
    if l == " ":
        msg1 = msg1 + " "
        continue
    c = ord(l)
    nova_l = c + d
    if nova_l > 90 and nova_l <= 96:
        nova_l = nova_l - 26
    if nova_l >= 123 and nova_l <= 127:
        nova_l = nova_l - 26
    nova_l = chr(nova_l)
    msg1 = msg1 + nova_l

print (msg1)