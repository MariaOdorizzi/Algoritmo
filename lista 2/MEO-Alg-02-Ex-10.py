matricula = str (input ("Digite a sua matrícula:"))

AA = matricula [:2]
S = matricula [2:3]
DDD = matricula [4:] 

if len(matricula) >= 7:
    print("Matrícula inválida. Por favor, digite a matrícula no formato AASDDD.")
if  S == "1":
    S = "1º"
elif S == "2":
    S = "2º"
else:
    S = "Semestre inesistente" 

print (f"A matricula do aluno é {matricula}. Ele foi matriculado no ano {AA}, no {S} semestre.") 