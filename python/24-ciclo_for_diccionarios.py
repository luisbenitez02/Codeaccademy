'''El ciclo for en python es genial, pero podemos tambien usarlo en un
diccionario y el resultado tambien es genial!'''

Webster = {
     "Cerdo hormiguero" : "La estrella de un popular programa infantil de caricaturas.",
     "Bee" : "El sonido que hace una cabra.",
     "Alfombra": "Va en el piso.",
     "Pizca": "Una cantidad pequena."
    }

for i in Webster:
    print (Webster[i])#la i contiene cada clave, asi que mostraremos el valor
#asociado a ella en cada paso del bucle

#Que tal un ciclo for, combinado con un if, asi es que nos gustan las cosas!

A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
w=0
#la i contiene en valor de cada elemento del array
for i in A:
   if(i%2 ==0):
      print (i, 'es un numero par')
      w+=1
   else:
      print(i, 'NO es un numero par')
print('Hay', w, 'numeros pares')
