""" 
Escenario
Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos saber con qué 
frecuencia aparece cada letra en el texto. Tal análisis puede ser útil en criptografía, 
por lo que queremos poder hacerlo en referencia al alfabeto latino.

Tu tarea es escribir un programa que:

Pida al usuario el nombre del archivo de entrada.
Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y 
minúsculas se tratan como iguales).
Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos 
distintos de cero).
Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.

Suponiendo que el archivo de prueba contiene solo una línea con:

aBc

el resultado esperado debería verse de la siguiente manera:
a -> 1
b -> 1
c -> 1

Tip:
Creemos que un diccionario es un medio perfecto de recopilación de datos para almacenar los recuentos. Las letras pueden ser las claves mientras que los contadores pueden ser los valores.
"""
from os import strerror


FICHERO="main.py"

def main ():
    histograma = dict ()
    try:
        for line in open(FICHERO, 'rt'):
            for ch in line:
                if ch.isalnum():
                    if ch in histograma:
                        histograma [ch] += 1
                    else:
                        histograma [ch] = 1
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))

    letras = sorted(histograma.keys())
    
    #for key,value in histograma.items():
    #    print (f"El número de {key} es de {value}.")

    for i in letras:
        print (f"El número de {i} es de {histograma[i]}.")


if __name__ == "__main__":
    main ()
    