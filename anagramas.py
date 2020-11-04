def pedirtexto(num):
    t=input(f'Introduzca texto numero {num}: ')
    return t

def eliminar_espacios(cadena):
    sin_espacios=""

    for i in cadena:
        if not i.isspace():
            sin_espacios = sin_espacios+i
    
    return sin_espacios.lower()

def comprobar(s1, s2):
    l1=[i for i in s1]
    l2=[i for i in s2]
    for i in l1:
        try:
            l2.remove(i)
        except:
            return False

    return l2 == []

if __name__ == "__main__":
    texto1=pedirtexto(1)
    texto2=pedirtexto(2)
    texto1=eliminar_espacios(texto1)
    texto2=eliminar_espacios(texto2)
    result=comprobar(texto1, texto2)
    if result:
        print ('OK')
    else:
        print ('NOT OK')