'''Los bucles for pueden tener una sentenica else asociada, esta solo se ejecutara
si y solo si el ciclo for se ejecuta correctamente y sin interrupciones por ejemplo un
break dentro de un if que lo detenga'''

#el else se encuentra al mismo nivel del for y NO identado

frutas = ['banano', 'manzana', 'naranja', 'tomate' ,'pera', 'uva']

print ('Tienes...')
for f in frutas:
   if f == 'tomate':
      print ('El tomate no es una fruta') #de hecho es.
      break#salta el bucle y detiene el codigo------------------------------
   print ('a', f)	
'''El else se ejecuta si y solo si el bucle termina correctamente de lo contrario se lo salta
y continua con la siguiente instruccion no if-else'''
else: #Si lo detuvo no se termina de ejecutar la siguientes lineas
   print('Una selección exclusiva de frutas')

#continua estas lineas normalmente

print('Esto acabo')

#quita tomate de la lista y date cuenta o mira este:

dulces= ['kit-kat','lime-pay','jelly-bean','pizza','candy of ron', 'chocolate']

print('Amo los dulces, te gustan estos')
for i in dulces:
    if i== 'pizza':
        print('Upps esto no es un dulce, estas bien')
        break
    print(i)
else:
    print('Son las versiones de Android, Chocolate no es una pero deberia')
   
