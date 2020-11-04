
def pedir_cadena():
    cadena=input('Introduzca la cadena a comprobar: ')

    return cadena

def eliminar_espacios(cadena):
    sin_espacios=""

    for i in cadena:
        if not i.isspace():
            sin_espacios = sin_espacios+i
    
    return sin_espacios.lower()



if __name__ == "__main__":
    cadena=pedir_cadena()
    sin_espacios=eliminar_espacios(cadena)
    sin_espacios_reverse=sin_espacios[::-1]

    if sin_espacios==sin_espacios_reverse:
        print ("Es un palindromo")
    else:
        print ("No es un palindromo")