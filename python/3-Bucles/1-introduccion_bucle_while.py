from random import randint
regla= True

while regla:#tambien se puede escribir: while regla== True
   print('No es necesario que la condicion True se escriba explicitamente')
   regla= False

num=1
while num<=10:
   print(num**2)
   num+=1

choice = input('Disfrutas el curso (y/n)')

while choice != 'y' and choice != 'n':
    choice = input("Lo lamento, no entendi eso.  Ingresalo de nuevo: ")

print('Ingresaste el dato correctamente')

'''Bucles infinitos, ha sido detenido por un ify BREAK'''
recuento = 0
while True:#mientras sea verdadero (siempre lo sera)
	print (recuento)
	recuento += 1#aumentamos y luego cuando llegue al tope saltamos con break
	if recuento >=10:
		break

'''Bucle games'''

print ("Numeros de la suerte Se generaran 3 numeros.")
print ("Si uno de ellos es '5', pierdes")

recuento = 0
while recuento < 3:
	num = randint(1, 6)
	print (num)
	recuento += 1
	if num == 5:
		print ("Lo lamento, tu pierdes")
		break
else:
   print ("Tu ganas")
