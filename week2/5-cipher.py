
def caesarCipher(s,k ):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    Alphabet = [i.upper() for i in alphabet]
    stri = list(s)
    for i in range(len(stri)):
        if stri[i] in alphabet:
            stri[i] = alphabet[(alphabet.index(stri[i])+k)%26]
    
    for i in range(len(stri)):
        if stri[i] in Alphabet:
            stri[i] = Alphabet[(Alphabet.index(stri[i])+k)%26]
    
    return "".join(stri)

s = "middle-Outz"

caesarCipher(s,2)
