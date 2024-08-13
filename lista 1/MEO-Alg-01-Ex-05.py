vasilhames_litro_menos = float(input ("Quantos vasilhames de um litro ou menos será retornado?"))
vasilhames_mais_litro = float(input ("Quantos vasilhames de mais de um litro será retornado?"))

valor_total = (vasilhames_litro_menos * 0.10) + (vasilhames_mais_litro * 0.25)

print ("O valor total dos créditos referentes ao retorno dos vasilhames é R$ {:.2f}". format(valor_total))