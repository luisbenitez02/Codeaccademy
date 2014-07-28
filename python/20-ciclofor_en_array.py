"""La estructura de un for se define asi:
   for variable in listas:
       "variable" corresponde a cada elemento dentro de la lista y NO es consecutivo como 1,2,3...
       solo devuelve el valor por el cual ha pasado y cuando no hay mas se acaba el bucle
"""

mi_lista = [1,9,3,8,5,7]
for numero in mi_lista:
    print("El numero es", numero)#numero corresponde a lo que esta adentro del array, no es consecutivo
    print(2*numero)#multiplicamos por cada numero, el bucle se auto regula y para


lista_inicial = [5, 3, 1, 2, 4]
lista_cuadrado = []

for i in lista_inicial:#la i es cada numero dentro de lista_inicial y NO la definimos ni nada
    lista_cuadrado.append(i**2)#agregamos al final de la lista
    lista_cuadrado.sort()#ORDENAMOS DE MENOR A MAYOR o alfabeticamente

print (lista_cuadrado)
