import re
import string

def sacar_digito_vida(num):

    while num>9:
        
        ln=[int(i) for i in (str(num))]
        num=sum(ln)

    return num

def pedir_fecha():

    fecha=input('Introduce tu fecha de nacimiento: ')
    patron=re.compile(r'^\s*\d{7,8}\s*')
    f=patron.match(fecha).group().strip()

    return int(f)



if __name__ == "__main__":
    fecha=pedir_fecha()
    d = sacar_digito_vida(fecha)
    print (d)

    pos()