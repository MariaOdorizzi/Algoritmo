def tokenização(n):
    l = []
    ant = ""
    num = ""
    for elem in n:
        if ((elem == "(")
            or (elem == ")")
            or (elem == "*")
            or (elem == "/")
            or (elem == "^")
            or (elem == "+" or elem == "-")
            and (ant.isnumeric() or ant == ")")):
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
    n = input ("Digite uma expressão matematica:")
    tokens = tokenização(n)
    print (tokens)

main()