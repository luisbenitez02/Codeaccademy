hola= ['hola','Qhubo','hello','hi','aloha','hola','hola','bona tarde','hola']

def holacount(hola):
   contador=0#para saber cuantas veces se repite algo, por ejemplo
   for i in hola:
      if i=='hola':
         contador+=1
   print('Se registraron', contador, 'strings con la palabra hola')

holacount(hola)#ejecutamos funcion con la variable hola que tiene arrays

"""Espacios en blanco"""
print()
print()

for l in "Programar":
   print(l)#imrpimiremos cada letra del string

for w in ("is cool"):#cuando w sea una s imprimiremos es genial!
   if w=='s':
      print('Es Genial!')
   
