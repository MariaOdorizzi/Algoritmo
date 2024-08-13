valor_suco = float(input ("Qual é o valor do suco? "))
valor_prato_principal = float(input ("Qual é o valor do prato principal"))
valor_sobremesa = float(input ("Qual é o valor da sobremesa?"))

valor_total = (valor_suco) + (valor_prato_principal) + (valor_sobremesa)

print ("O valor total dessa refeição é R$ {:.2f}". format(valor_total))