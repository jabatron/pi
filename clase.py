class conClase():
    def visible(self):
        print ("visible")
        
    def __oculto(self):
        print("oculto")
obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")
    
obj.conClase.__oculto()
