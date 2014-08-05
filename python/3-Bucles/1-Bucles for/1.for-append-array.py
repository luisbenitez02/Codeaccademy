pasatiempos = []

for i in range(3):
    hobby= input('Escribe un pasatiempo')
    pasatiempos.append(hobby)

print(pasatiempos)#fueron agregados exitosamente al array

'''Tambien podemos tomar una letra o imprimirlas una por una con los ciclos for'''
pais= 'Colombia'
for c in pais:
   if c == 'o':
      print('OO')
   else:
      print(c)

numeros  = [7, 9, 12, 54, 99]

print ("Esta lista contiene: ")
for num in numeros:
    print (num)

for w in numeros:
    print(w**2)
