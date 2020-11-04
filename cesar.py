
import string

def pedir_texto():
    cadena=input('Introduce una cadena a codificar: ')
    gap=input('Desplazamiento: ')
    
    return cadena, int(gap)

def swap_letter(character, gap):

    if character.islower():
        pos=string.ascii_lowercase.find(character)
        new_pos=pos+gap
        new_char=string.ascii_lowercase[new_pos%26]
        return new_char
    elif character.isupper():
        pos=string.ascii_uppercase.find(character)
        new_pos=pos+gap
        new_char=string.ascii_uppercase[new_pos%26]
        return new_char

    return character

def codificar_texto(texto, gap):
    codificado = ""
    c=""

    for i in texto:

        c = swap_letter(i, gap)
        codificado=codificado+c

    return codificado

def mostrar_texto(texto):
    print (f'el texto codificdo es: {texto}')
    


if __name__ == "__main__":
    texto, gap = pedir_texto()
    
    codificado = codificar_texto(texto, gap)
    mostrar_texto(codificado)