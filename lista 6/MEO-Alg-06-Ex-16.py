def precedencia(oper):
    if oper == "+" or oper == "-":
        return 1
    elif oper == "*" or oper == "/":
        return 2 
    elif oper == "^":
        return 3
    else:
        return -1

def conversao(infix):
    opers = []
    postfix = []
    precToken = ""
    for token in infix:
        if token [0:].isdigit() or (token [0] == "-" and token [1:].isdigit()) or (token [0] == "+" and token [1:].isdigit()):
            postfix.append(token)
        elif token == "*" or token == "/" or token == "^" or token == "+" or token == "-":
            while len(opers) > 0 and opers [-1] != "(" and precedencia(token) < precedencia(opers [-1]):
                postfix.append(opers [-1])
                opers.remove(-1)
            opers.append(token)
        elif token == "(":
            opers.append(token)
        elif token == ")":
            while opers [-1] != "(":
                postfix.append(opers [-1])
                opers.remove(opers[-1])
            opers.remove ("(")

    while len(opers) >= 1:
        postfix.append(opers [-1])
        opers.remove(opers [-1])
    return postfix

def tokenizaçao(n):
    l = []
    ant = ""
    num = ""
    for elem in n:
        if elem == "(" or elem == ")" or elem == "*" or elem == "/" or elem == "^" or elem == "+" or elem == "-" and (ant.isnumeric() or ant ==")"):
            if num != "":
                l.append(num)
                num = ""
            l.append(elem)
        else:
            num += elem
        ant = elem
    if num != "":
        l.append(num)
        num = ""
    return l

def main():
    n = input ("Digite uma expressão matemática:")
    infix = tokenizaçao(n)
    print (conversao(infix))

main()