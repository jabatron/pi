""" 
    practica clases y pila
"""

class Pila():
    def __init__ (self):
        self.__pila=[]
        self.__len=0

    def __str__ (self):
        if self.tamaño == 0:
            return "pila vacia."
        else:
            return self.__pila[-1]

    @property
    def tamaño(self):
        return self.__len

    
    def push(self, element):
        self.__pila.append(element)
        self.__len+=1

    def pop (self):
        if self.tamaño == 0:
            return "pila vacia."
        else:
            p = self.__pila[-1]
            del self.__pila[-1]
            self.__len-=1
            return p



def main ():
    p = Pila()
    p.push ("hola")
    p.push (("a", "b"))
    p.push ({"temp":30, "humidity":40})
    p.push ("adios")
    print (p)
    print(p.tamaño)
    print (p.pop ())
    print (p.pop ())
    print (p.pop ())
    print (p)
    
    



if __name__ == "__main__":
    main ()
