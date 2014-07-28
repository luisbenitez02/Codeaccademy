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
#al final general el tablero

def fila_aleatoria(tablero):
    '''Retornara una posicion de fila aleatoria, alli esta el barco'''
    return (random.randint(0,len(tablero)-1))# un numero aleatorio de 0 a 4
#servira por si queremos ampliar el tablero

def columna_aleatoria(tablero):
    '''Retorna una posicion de columna aleatoria'''
    return(random.randint(0,len(tablero[0])-1))#se hace asi para que el numero JAMAS sea cual sea
#la dimension del tablero el numero sobrepase

print_tablero(tablero)#mostremos el tablero de juego

print('esta en la fila',fila_aleatoria(tablero))#-------------------------------------------------->debug
print('esta en la columna',columna_aleatoria(tablero))#----------------------------------------------->debug

adivina_fila= input('¿En que fila esta el barco Capitan?')
adivina_columna= input('¿En que columna esta el barco Capitan')
