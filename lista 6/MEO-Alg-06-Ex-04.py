codMorse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

def caracteres(f):
    fScaracteres = ""
    for i in f:
        if i == "," or i == "." or i == "!" or i == " " or i == "?":
            continue
        else:
            fScaracteres = fScaracteres + i
    ffinal = fScaracteres.upper()
    return ffinal

def codificar(f, dicionario):
    fcodifica = ""
    for i in f:
        if (i in dicionario) == True:
            l_morse = dicionario.get(i)
            fcodifica = fcodifica + " " + l_morse
    return fcodifica

def main():
    f = input ("Digite uma frase:")
    f1 = caracteres(f)
    print (codificar(f1, codMorse))

main()