length = len(str(45))#convierte a 45 en un numero
print (length)#cuantos caracteres tiene ese string (en length o.O)

def cuadrado(n):#le pasamos el parametro n
    """llevamos el numero ingresado al cuadrado"""
    al_cuadrado = n**2
    print ("%d al cuadrado es %d." % (n, al_cuadrado))
    #formateamos como numero %d
    return al_cuadrado
    
#le pasamos el parametro es n, pero el argumento es 10
cuadrado(10)#

"""Ahora le pasamos dos parametros y los dos argumentos 37 y 4"""
def potencia(base,exponente):
    resultado = base**exponente
    print ("%d a la %d potencia es %d." % (base, exponente, resultado))

potencia(37,4)



"""MULTIPLES ARGUMENTOS"""
#Cuando no sabemos cuantos argumentos vamos a pasar, le entregamos *args
#significa que no sabemos cuantos van a venir pero que los use
#es *args por convencion pero puede ser *amor, lo importante es que le
#preceda el asterisco al declarar como parametro
def actores_favoritos(*args):
    """Muestra tus actorES favoritoS (¡en plural!)"""
    print ("Tus actores favoritos son:" , args)
    
    
actores_favoritos("Michael Palin", "John Cleese", "Graham Chapman")


"""FUNCIONES QUE LLAMAN FUNCIONES"""
def amor_con_amor(k):
    k+1#esta mal mira el ejemplo 8 de la misma carpeta
    
def se_paga(amor_con_amor):
    k+2
    print(k)
    
amor_con_amor(8)
