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
Creemos que un diccionario es un medio perfecto de recopilación de datos para almacenar los recuentos. 
Las letras pueden ser las claves mientras que los contadores pueden ser los valores.

VERSION2
El código anterior necesita ser mejorado. Está bien, pero tiene que ser mejor.

Tu tarea es hacer algunas enmiendas, que generen los siguientes resultados:

El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero).
El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión '.hist' (debe concatenarse con el nombre original).
Suponiendo que el archivo de prueba contiene solo una línea con:

cBabAa

El resultado esperado debería verse de la siguiente manera:
a -> 3
b -> 2
c -> 1

Tip:

Emplea una lambda para cambiar el ordenamiento.
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

    print (histograma)

    histograma = dict(sorted(histograma.items(),key=lambda item : item[1], reverse=True))
    
    print (histograma)

    for key,value in histograma.items():
        print (f"El número de {key} es de {value}.")

    #for i in histograma.keys:
    #    print (f"El número de {i} es de {histograma[i]}.")

    FICHERO_HIST = FICHERO+".hist"
    try:
        file_hist=open (FICHERO_HIST, 'wt')
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))
    else:
        for key,value in histograma.items():
            file_hist.writelines (f"{key}-->{value:3}\n")
        file_hist.close ()


if __name__ == "__main__":
    main ()
    