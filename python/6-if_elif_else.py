import random

col= random.random()*100

if col <= 25:
    print("El numero " + str(col) + " Es menor que 25")
elif col<=50:
    print("El numero " + str(col) + " Es menor que 50")
else:
    print("El numero " + str(col) + " es mayor que 50")
