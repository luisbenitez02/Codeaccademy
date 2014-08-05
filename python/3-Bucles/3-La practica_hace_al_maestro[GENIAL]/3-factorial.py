'''Definiremos el fatoiral de cualquier numero'''
def factorial(num):
   factor=1 #empezamos con el 1 para multiplicar sin que de 0
   while num > 0 :#mientras el numero sea mayor que 0
      factor*=num#el factor variara y sera multiplicado por el numero
      num-=1#el numero reducira, a cada vuelta se multiplicara
      #por lo contenido en factor
   print(factor)#se imprime al final

factorial(5)

      
