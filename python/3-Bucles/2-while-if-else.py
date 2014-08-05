from random import randrange

numero_aleatorio = randrange(1, 10)
print(numero_aleatorio)

count = 0
while count < 3:
    print("Contador",count)
    adivina=int(input('Adivina un numero:'))
    count+=1

    if adivina == numero_aleatorio:
        print("Tu ganas")
        break
    else:
        print('Tu pierdes')

