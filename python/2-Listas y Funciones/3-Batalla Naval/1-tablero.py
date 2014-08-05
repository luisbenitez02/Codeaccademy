import random #para usar algunas funciones

tablero = []#almaceno todo el tablero

for x in range(0,8):#mientras estemos dentro de un rango de 0 a 8(cuenta hasta 7 en impresion)
  tablero.append(["O"] * 8)#Agregamos un nuevo array
'''Esto formara un tablero de puras ['o','o','o']de 5*5'''
#print(tablero)---------------------------------------------------------------->debug

def print_tablero(tablero):
  for i in tablero:
      print(" ".join(i))#¿Que hace Join? esta concatenando toda la fila
#en un solo array, asi para cada bucle imprime una fila sin comillas
#al final genera el tablero

print_tablero(tablero)#mostremos el tablero de juego
#print(len(tablero))#---------------------------->debug

def fila_aleatoria(tablero):
    '''Retornara una posicion de fila aleatoria, alli esta el barco numero 1'''
    return (random.randint(0,len(tablero)-1))# un numero aleatorio de 0 a 5 servira por si queremos ampliar el tablero

def fila_aleatoria_two(tablero):
  '''Retornara una posicion de fila aleatoria, alli esta el barco numero 2'''
  return (random.randint(0,len(tablero)-1))# un numero aleatorio de 0 a 5

def columna_aleatoria(tablero):
    '''Retorna una posicion de columna aleatoria'''
    return(random.randint(0,len(tablero[0])-1))#se hace asi para que el numero JAMAS sea cual sea la dimension del tablero el numero sobrepase

def columna_aleatoria_two(tablero):
    '''Retorna una posicion de columna aleatoria'''
    return(random.randint(0,len(tablero[0])-1))

def grand_fila_aleatoria(tablero):
  return (random.randint(1,len(tablero)-2))

def grand_col_aleatoria(tablero):
  return(random.randint(1,len(tablero[0])-2))

barco_fila=0
barco_col=0

barco_fila_two=0
barco_col_two=0

gran_barco_fila=0
gran_barco_col=0

cont_gran_barc_fil=0
cont_gran_barc_col=0

while barco_fila==barco_fila_two and barco_col==barco_col_two:
  barco_fila= fila_aleatoria(tablero)
  barco_col= columna_aleatoria(tablero)
  
  barco_fila_two= fila_aleatoria_two(tablero)
  barco_col_two= columna_aleatoria(tablero)

while gran_barco_fila == gran_barco_col or gran_barco_fila==barco_fila and gran_barco_col==barco_col or :
  gran_barco_fila= grand_fila_aleatoria(tablero)
  gran_barco_col= grand_col_aleatoria(tablero)

jueguito= random.randint(0,5)
if jueguito == 0:
  cont_gran_bar_fil= gran_barco_fila + 1
  cont_gran_barc_col= gran_barco_col + 1
  
elif jueguito == 1:
  cont_gran_bar_fil= gran_barco_fila - 1
  cont_gran_barc_col= gran_barco_col - 1
  
elif jueguito == 2:
  cont_gran_bar_fil= gran_barco_fila - 1
  cont_gran_barc_col= gran_barco_col

elif jueguito == 3:
  cont_gran_bar_fil= gran_barco_fila + 1
  cont_gran_barc_col= gran_barco_col

elif jueguito == 4:
  cont_gran_bar_fil= gran_barco_fila 
  cont_gran_barc_col= gran_barco_col - 1

elif jueguito == 5:
  cont_gran_bar_fil= gran_barco_fila 
  cont_gran_barc_col= gran_barco_col + 1
  

print('El barco 1, esta en la posicion[fila][columna]:',barco_fila,barco_col)#-------------------------------------------------->debug
print('El barco 2, esta en la posicion[fila][columna]:',barco_fila_two,barco_col_two)

##-----------------------------------Ejecutaremos el juego con 4 oportunidades
##for turno in range(5):
##   if turno == 3:
##      print(str(turno+1),'turno, Ups! Es tu ultima oportunidad...')
##   elif turno== 4:
##     print('¡Perdiste esta batalla!, Ahora yo gobernare los 6 mares, digo 7...')
##     break
##   else:
##      print('turno #',str(turno+1))
##   adivina_fila= int(input('¿En que fila esta el barco Capitan?'))#convertimos la entrada en un numero entero
##   adivina_columna= int(input('¿En que columna esta el barco Capitan'))
##
##   #------------------------------------sentencias if-else para controlar la respuesta del juego
##   if adivina_fila==barco_fila and adivina_columna==barco_col:
##       print("Felicitaciones Hundiste mi barco")
##       break #detiene el bucle
##   else:
##      if adivina_fila>4 or adivina_fila<0 or adivina_columna>4 or adivina_columna<0:
##         print('Has tocado tierra, acercate a la batalla de los 7 mares!')
##         
##      elif tablero[adivina_fila][adivina_columna]=='X':
##         print('anda, ya dijiste esa')
##      else:
##         tablero[adivina_fila][adivina_columna]='X'
##         #imprime el tablero con la nueva x
##      print('JAJA! Fallaste!')
##
##   print_tablero(tablero)
