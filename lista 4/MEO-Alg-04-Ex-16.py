import random

n_simulação = 10
tt_sorteios = 0
resultados = []

for i in range (n_simulação):
    sequencia = ""
    sorteios = 0
    while "AAA" not in sequencia and "OOO" not in sequencia:
        resultado = random.choice(["A", "O"])
        sequencia += resultado
        sorteios += 1
    print (f"{sequencia}, ({sorteios} sorteios)")
    resultados.append(sorteios)
    tt_sorteios += sorteios

md_sorteios = tt_sorteios / n_simulação
print (f"\nNa média, foram necessários {md_sorteios:.1f} sorteios.")