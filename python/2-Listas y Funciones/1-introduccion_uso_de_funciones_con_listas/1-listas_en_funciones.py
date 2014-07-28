n=[5,4,7,8,9]
print('Lista original:',n)
def sumitas(x):
#una funcion que toma una lista
   print('podemos imprimir un elemento de la lista:',x[1])
   x[0]+=5
   x.append(20)
   print('modificarlo en tiempo de ejecucion:', x[0])
   print('E incluso agregar un nuevo elemento, añadimos el 20 al final')
   return('la lista es:',n)

print(sumitas(n))

frases=['Hola','Chao','Rehola','Q mas?','Parceros','Feos','amor']

def imprimir(lista):
   count=0
   for i in lista:
      count+=1
      print(i)
   print('Numero de elementos:',count)

imprimir(frases)

numeros=[2,4,6,8]

def doble(m):
   #mientras estes dentro del rango que empieza en 0 y termina
   #cuando no hallan mas argumentos en la variable haz:
   for i in range(0,len(m)):
      m[i]*=2
      print(m)#imprimimos toda la lista, vemos en cada bucle como
#multiplicamos uno por uno

doble(numeros)

#--------------------------------------------------------------------------
'''Pasar un rango a una funcion SIN FUNCIONAR'''
##def rangitos(p):
##    for i in p:
##        p[i]*= 2
##    return (p)
##
##print (rangitos(range(0,3)))

#-------------------------------------------------------------------------
s = ["Michael","Lieberman"]#string comun
def myFun(v):
    texto=""#contiene los string, variable por ahora vacia
    for i in v:
        texto+=i#con cada paso se le agrega el string contenido en la i a la variable
    return(texto)

print (myFun(s))
