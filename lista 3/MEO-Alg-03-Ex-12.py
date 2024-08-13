ano = int (input ("Digite um ano:"))

if ano % 400 == 0:
    texto = "é bissexto"
elif ano % 100 == 0:
    texto = "não é bissexto"
elif ano % 4 == 0:
    texto = "é bissexto"
else:
    texto = "não é bissexto"
print(f"O ano {ano} {texto}.")