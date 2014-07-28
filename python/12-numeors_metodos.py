def numeros(*args):
    print(max(args))#maximo de una cadena
    print(min(args))#minimo de una cadena

def distancia_desde_cero(arg):
    print(abs(arg))#imprime la distancia que tiene el numero desde el 0
                    #en valor absoluto, SOLO TOMA UN NUMERO

numeros(10,-10,5,-5,4)
distancia_desde_cero(-20)

print(type(20))
print(type(2.8))
print(type("Hola a todos!"))
