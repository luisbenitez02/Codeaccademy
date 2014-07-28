'''Aprende sobre los diccionarios, estas son diversas formas y todas validas de crear un diccionario'''
#fijate como dentro de un diccionario metemos un array asignado a una clave. Que loco no?

inventario={'plata': 'cadena', 'manilla de acero': 800, 'oro':['collar', 'pulsera', 'manubrio'], 'patatas':500}
print('El diccionario inventario contiene:',inventario)
#y tambien puedes añadir nuevos arrays a un diccionario, incluso despues de haberlo definido
inventario['chocolate']= ['ositos', 'corazones', 'palitos']
#se conforma por: nombre_diccionario['nuevaclave']=['nuevos', 'valores', 'en array']

inventario['oro'].sort()#ordenamos los valores dentro del diccionario inventario > clave oro > array

print('Ahora con la clave oro ordenada tenemos: \n ', inventario['oro'],'ah y no olvidemos lo que acabamos de agregar:\n',inventario['chocolate'])
print('Quien quiere un manubrio de oro?, borremoslo')

inventario['oro'].remove('manubrio')
print(inventario['oro'])

print('Ese valor de alli, por unas patatas', inventario['patatas'],'debe ser una broma sumale otros 500')
inventario['patatas']+=500
print(inventario['patatas'])

#Si ponemos un int dentro de un array de strings nos dara un error de conversion al querer imprimir
#la funcion remove resulta util cuando se tiene este tipo de diccionarios con arrays
# la funcion "del" elimina un conjunto {clave:valor} teniendo como parametro la clave
#la funcion remove() elemina un conjunto {clave:valor} teniendo como parametro la clave
