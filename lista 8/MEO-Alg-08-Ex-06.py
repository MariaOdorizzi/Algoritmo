def mdc (a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return mdc (b, c)

def mdc2 (a, b):
    return a if b == 0 else mdc(b, a % b)

print (mdc2 (18, 60))