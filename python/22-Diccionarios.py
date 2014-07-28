agenda= {"Patricia":2746886, "Luis":3154960166,"Angelica":317623589,"Hernando"
         :3176231081}

print("El numero de patricia es", agenda["Patricia"])
print("Y el de Luis es:", agenda["Luis"])

for i in agenda:# la i aqui corresponde a los nombres y no a sus elementos
   print(i)

#PODEMOS AGREGAR NUEVOS ELEMENTOS A UN DICCIONARIO VACIO:
edad={}#diccionario vacio
print(edad)

edad["Amelia"]=20#añadimos un nuevo valor al diccionario
edad["Luis"]=19
edad["Pablo"]=15
edad["Juan"]=17
print(edad)

print(edad["Amelia"])
print("Hay", str(len(edad)),"entradas par de nombre y edad")

"""Podemos cambiar valores y eliminarlos"""
#del elimina un par clave valor
del agenda["Angelica"]#elimanmos a angelica del diccionario

agenda["Luis"]= 3214602868#cambiamos a luis, le dimos otro numero

print(agenda)
