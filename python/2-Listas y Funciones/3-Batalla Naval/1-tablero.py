import random #para usar algunas funciones

tablero = []#almaceno todo el tablero

for x in range(0,5):#mientras estemos dentro de un rango de 0 a 5(cuenta hasta 4)
  tablero.append(["O"] * 5)#Agregamos un nuevo array
'''Esto formara un tablero de puras ['o','o','o']de 5*5'''
#print(tablero)---------------------------------------------------------------->debug

def print_tablero(tablero):
  for i in tablero:
      print(" ".join(i))#¿Que hace Join? esta concatenando toda la fila
#en un solo array, asi para cada bucle imprime una fila sin comillas
#al final genera el tablero

print_tablero(tablero)#mostremos el tablero de juego

def fila_aleatoria(tablero):
    '''Retornara una posicion de fila aleatoria, alli esta el barco'''
    return (random.randint(0,len(tablero)-1))# un numero aleatorio de 0 a 4
#servira por si queremos ampliar el tablero

def columna_aleatoria(tablero):
    '''Retorna una posicion de columna aleatoria'''
    return(random.randint(0,len(tablero[0])-1))#se hace asi para que el numero JAMAS sea cual sea
#la dimension del tablero el numero sobrepase



barco_fila= fila_aleatoria(tablero)
barco_col= columna_aleatoria(tablero)

#print('esta en la fila',barco_fila)#-------------------------------------------------->debug
#print('esta en la columna',barco_col)#----------------------------------------------->debug

#-----------------------------------Ejecutaremos el juego con 4 oportunidades
for turno in range(5):
   if turno == 3:
      print(str(turno+1),'turno, Ups! Es tu ultima oportunidad...')
   elif turno== 4:
     print('¡Perdiste esta batalla!, Ahora yo gobernare los 6 mares, digo 7...')
     break
   else:
      print('turno #',str(turno+1))
   adivina_fila= int(input('¿En que fila esta el barco Capitan?'))#convertimos la entrada en un numero entero
   adivina_columna= int(input('¿En que columna esta el barco Capitan'))

   #------------------------------------sentencias if-else para controlar la respuesta del juego
   if adivina_fila==barco_fila and adivina_columna==barco_col:
       print("Felicitaciones Hundiste mi barco")
       break #detiene el bucle
   else:
      if adivina_fila>4 or adivina_fila<0 or adivina_columna>4 or adivina_columna<0:
         print('Has tocado tierra, acercate a la batalla de los 7 mares!')
         
      elif tablero[adivina_fila][adivina_columna]=='X':
         print('anda, ya dijiste esa')
      else:
         tablero[adivina_fila][adivina_columna]='X'
         #imprime el tablero con la nueva x
      print('JAJA! Fallaste!')

   print_tablero(tablero)

