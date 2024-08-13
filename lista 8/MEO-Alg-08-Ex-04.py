def fibonacci(n):
    dic = {}
    if n <= 0:
        return 0
    elif n == 1 :
        return 1 
    else:
       return memorizacao(n, dic)
   
def memorizacao(n,dic):
    if n in dic:
        return dic[n]
    else:
        resposta = fibonacci(n - 1) + fibonacci(n - 2)
        dic[n] = resposta
        return resposta

def main():
    n = int (input ("Digite um número para fatorar:"))
    resultado = fibonacci(n)
    print (resultado)

main()