'''Vamonos de compras, veras que genial es este ejercicio'''

'''En este ejercicio podemos ver como trabajar a la par con una variable que contiene un array
y dos variables que contienen diccionarios, el resultado sumado con un ciclo for y un if nos da una
genial aplicacion para hcer nuestras comprar en una tienda'''

#primero llevemos nuestra lista de componentes para armar una super pc
lista_componentes=['motherboard','procesador','tarjeta grafica','tarjeta de red']

#El almacen tiene pocas unidades, este es su inventario DICCIONARIO:
inventario={'motherboard':4,'tarjeta grafica':1,'tarjeta de red':0,'procesador':2,}

#y los precios son los siguientes DICCIONARIO:
precios={'motherboard':1500,'tarjeta grafica':100,'tarjeta de red':800,'procesador':1200}

def mis_cuentas(lista_componentes):
   total=0
   for i in lista_componentes:#la var i contiene el string de la lista_componentes
      if inventario[i]>0:#si en inventario esta esa palabra y es mayor que 0, entonces agregala al carro!
         total+=precios[i]#entonces sumame eso a mi cuenta
         inventario[i]-=1#y restale uno al inventario
   return total

print('En total debo invertir unos:',mis_cuentas(lista_componentes))
print('Esto fue lo que quedo en el inventario:', inventario)
