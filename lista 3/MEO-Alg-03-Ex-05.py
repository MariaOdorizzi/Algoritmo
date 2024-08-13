mes = str (input ("Digite um mês:"))

if mes.lower() == 'janeiro' or mes.lower() == 'março' or mes.lower() == 'maio' or mes.lower() == 'julho' or mes.lower() == 'agosto' or mes.lower() == 'outubro' or mes.lower() == 'dezembro':
   print (f"O mês de {mes} possui 31 dias.")  
elif mes.lower() == 'abril' or mes.lower() == 'junho' or mes.lower() == 'setembro' or mes.lower() == 'novembro':
    print (f"O mês de {mes} possui 30 dias.") 
elif mes.lower() == 'fevereiro':
   print (f"O mês de {mes} possui 28 ou 29 dias.")