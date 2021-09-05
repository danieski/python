
# Queremos codificar una palabra
def codificador(frase):
    encriptada = ""
    for letra in frase:
        if letra in "aeiou":
            if letra is "AEIOU":
                encriptada = encriptada + "Z"
            else:
                encriptada = encriptada + "z"
        else :
            encriptada = encriptada + letra
    return encriptada



print(codificador(input("Ponga algo: ")))

