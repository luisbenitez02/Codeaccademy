'''identificaremso si un numero es o no primo'''
def es_primo(x):
   if x <= 1:#menor o igual a uno NO ES PRIMO
      return(False)
   c=0#contador
   for i in range(1,x):#del 1 al x(por ejemplo 2)
      if x%i==0:#si la division en el recorrido da 0 residuo e sun numero divisible
         c+=1
   if c>1:
      return(False)#si mas de un numero lo divide entonces NO ES PRIMO
   else:
      return(True)
#el mismo numero no se contabiliza aqui
print(es_primo(4))
