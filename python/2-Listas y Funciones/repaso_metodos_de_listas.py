'''Repasemos un poco los metodos de las listas'''
n=[5,4,8,6,2]
print(n)
#podemos borrar con la funcion del
del n[0]
print(n)

#o con el metodo pop, le pasamos el indice
n.pop(2)
print(n)

#funciones de DOS ARGUMENTOS
def myFun(m,n):
   return m+n

m= int(input('ingresa un primer numero a sumar'))
n= int(input('ingresa un segundo numero a sumar'))

print(myFun(m,n))

#funciones INFINITOS ARGUMENTOS
def calcula(*numeros):
   return sum(numeros)

print('Suma de todos los argumentos',calcula(5,4,7,8,7,8,9,8,7))
