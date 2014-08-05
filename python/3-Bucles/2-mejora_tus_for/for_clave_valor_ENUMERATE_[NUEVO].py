golosinas= {'jumbo mani':350, 'malvaviscos':50, 'Nutella':600, 'Galletas con crema':250}

for clave in golosinas:
   print(clave,'$'+ str(golosinas[clave]))

'''Que tal un menu? Un menu usando un nuevo metodo ENUMERATE'''

platos=['pizza', 'pasta', 'ensalada', 'nachos']
#EL METODO ENUMERATE proporciona un indice a cada elemento por el que el bucle itinera

print('Hoy tenemos los siguientes platillos:')
for num_indice, platillo in enumerate(platos):#num_indice contiene en numero del elemento en el array
   print(str(num_indice+1)+'.',platillo)




