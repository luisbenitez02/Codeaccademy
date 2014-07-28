#una lista con los animales de Zoo
zoo_animals= ["Pinguinos", "Nutria", "Elefante", "Lemures"]
print("El cuarto animal es " + zoo_animals[3])

#bucle while que imprime todos los registros de animales existentes

#con len, obtenemos la longuitud de esa lista
for i in zoo_animals:
   print("Usando el ciclo for, tenemos: \n ",i)
   
"""Vamos a agregar un nuevo elemento con la funcion""" #append
habitat=["hielo", "estanque", "selva", "Brinca, brinca"]
#cambiamos el habitat 3 para mover el bote
habitat[3]= "Mover el bote"

#agregamos super-divertido al final de array
habitat.append("Super-divertido")
print(habitat[3])
print("Aqui esta habitat y su array, con la funcion append" + str(habitat))

#podemos llamar solo algunos datos de arrays
maletin = ["gafas", "sombrero", "pasaporte", "portatil", "traje", "zapatos"]

#llamamos los dos primeros
primeros = maletin[0:2]
print(primeros)
#llamamos los elementos de la mitad
mitad = maletin[2:4]
print(mitad)
#llamamos los dos ultimos
ultimos = maletin[4:6]
print(ultimos)
#RECUERDA, que el primero SI se muestra y el segundo valor del array no
#se muestra, por tal para los dos ultimos nos pasamos en +1

#FORMAS de particionar un STRING
animales = "catdogfrog"
cat = animales[:3]#tres primeras letras
print(cat)
dog = animales[3:6]#tres letras de la mitad
print(dog)
frog = animales[6:]#del 6 en adelante hasta acabar
print(frog, 'y ya')
