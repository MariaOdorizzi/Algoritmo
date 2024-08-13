def tokenizacao(exp):
    l = []
    ant = ""
    num = ""
    for elem in exp:
        if (elem == "(") or (elem == ")") or (elem == "*") or (elem == "/") or (elem == "^") or (elem == "+") or (elem == "-") and (ant.isnumeric() or ant == ")"):
            if num != "":
                l.append(num)
                num = ""
            l.append(elem)
        else:
            num += elem
        ant = elem
    if num != "":
        l.append(num)
    return l

def conversao(infix):
    opers = []
    postfix = []
    precToken = ""
    for token in infix:
        if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
            postfix.append(token)
        elif (token == "*") or (token =="/") or (token == "^") or (token == "+") or (token == "-"):
            while len(opers) >= 1 and opers[-1] != "(" and precToken < opers[-1]:
                postfix.append(opers.pop())
            opers.append(token)
        elif token == "(":
            opers.append(token) 
        elif token == ")":
            while opers[-1] != "(":
                postfix.append(opers.pop())
            opers.pop()
        precToken = token
    while len(opers) >= 1:
        postfix.append(opers.pop())
    return postfix

def avaliar(lPosfix):  
    valor = []
    resposta = ""
    for token in lPosfix:
        if token.isdigit():
            valor.append(int(token))
        else:
            d = valor.pop()
            e = valor.pop()
            if token == '-':
                resposta = e - d
            elif token == '+':
                resposta = e + d
            elif token == '/':
                resposta = e / d
            elif token == '*':
                resposta = e * d
            else:
                return "ERRO: Operador inserido é inválido!"
            valor.append(resposta)
    return valor

def main():
    n = input("Digite uma expressão matemática: ")
    infix = tokenizacao(n)
    print(avaliar(conversao(infix)))

main()