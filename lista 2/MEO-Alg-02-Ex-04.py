n_1 = int (input ("Digite um numero:"))
n_2 = int (input ("Digite um numero:"))
n_3 = int (input ("Digite um numero:"))

max_n = max(n_1, n_2, n_3)
min_n = min(n_1, n_2, n_3)
med_n = (n_1 + n_2 + n_3) - max_n - min_n

print ("A ordem crescente do números dados é ", min_n, ",", med_n, ",", max_n,".")