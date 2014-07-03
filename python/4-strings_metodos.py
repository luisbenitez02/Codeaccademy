#Metodos de los Strings

loro= "Azul Noruego"
print(len(loro))#equivalente a .length()

#.lower() convierte todo un string a minusculas,
#Fijate que se usan diferente que len()
print (loro.lower())

#.upper() convierte todo a MAYUSCULAS

print (loro.upper())

"""las funciones .lower() y .upper() solo funcionan con strings,
por eso su sintaxis es distinta
a diferencia de srt() y len() estas funcionaan con variso tipos de objetos
por ello necesitan la variable como parametro"""
pi= 3.14159
print (str(pi))

#Formateo de strings con %, es muy interesante

camelot = 'Camelot'
lugar = 'lugar'
print ("No vayamos a %s. Es un %s tonto." % (camelot, lugar))

#Raw_input cambio a input, cuidado con los parentesis de print
nombre = input("Cuál es tu nombre")
mision = input("Cuál es tu mision")
color = input("Cuál es tu color favorito")

print ("Ah, asi que tu nombre es %s, tu mision es %s, \
y tu color favorito es %s." % (nombre, mision, color))
