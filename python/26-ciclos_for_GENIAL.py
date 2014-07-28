'''Que tal un bucle for que cruze dos listas, seria genial no?, vamos a ver'''

creditos_inscritos={'Juan':18,'Maria':17,'Estiben':15,'Carolina':20,'Kelly':12, 'Emmanuel':20,'Luis':18,'Patricia':17}

programa={'Juan':'Ing Ambiental','Maria':'Fisica Pura','Estiben':'Administracion','Carolina':'Contaduria','Kelly':'Enfermeria',
          'Emmanuel':'ing Sistemas','Luis':'Ing Sistemas','Patricia':'Periodismo'}


for i in creditos_inscritos:
   print (i,'\n',
          'inscribio:',creditos_inscritos[i],'creditos',
          '\n En el programa de:',programa[i])
#fijate que el orden de impresion en totalmente aleatorio

print('\n \n')

'''-------------------Fijate en otro ejemplo de inventarios--------------------------'''
precios = {
    "banano": 4,
    "manzana": 2,
    "naranja": 1.5,
    "pera": 3
    }
    
inventario = {
    "banano": 6,
     "manzana": 0,
     "naranja": 32,
     "pera": 15
    }
cuenta=0
for i in precios:
    print (i)
    print (' valor total de inventario:',precios[i]*inventario[i])
    cuenta+=precios[i]*inventario[i]
print ('En total podemos ganar:',cuenta,'si vendemos todo')

