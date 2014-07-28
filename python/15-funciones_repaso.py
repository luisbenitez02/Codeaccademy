import math

def cubo(x):

    return x**3

print(cubo(27))#imprimimos la funcion directamente
#Le pasamos argumento y todo a la funcion print
#esto imprime lo que esa funcion nos retorna

def esPar(w):
    if w%2==0:
        print("sip, es par")
        return "sip"
    else:
        print("nop, no es par")
        return "nop"
esPar(8)


def areaDeCirculo(radio):
    area= ((radio**2)* math.pi)
    print(area)
    return area

ingr= input("ingreso")
areaDeCirculo(float(ingr))
