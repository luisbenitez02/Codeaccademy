'''Sumaremos uno por uno los numeros ingresados, por ejemplo si ingresas 1234
tendras 1 + 2 + 3 + 4 = 10'''

def suma_de_digitos(n):
   suma=0
   
   while n != 0:
      suma+=n%10#tomamos el numero de la derecha y sumamos
      n=n//10#le quitamos el ultimo numero de la derecha por cada paso
      #al final del bucle el numeor ingresado es un 0, entonces termina
   return(suma)#retorna la suma de los digitos

print(suma_de_digitos(55555))
