def verificar(dia, mes, ano):
    digito = str (ano) [-2:]
    if int (dia * mes) == int (digito):
        return True
    return False

def main():
    diaI = 1
    mesI = 1
    anoI = 1901
    diaF = 31
    mesF = 12
    anoF = 2000

    for ano in range(1901, 2000):
        for mes in range(1, 12):
            for dia in range(1, 31):
                if verificar(dia, mes, ano):
                    print (f"{dia}/{mes}/{ano}")

main()