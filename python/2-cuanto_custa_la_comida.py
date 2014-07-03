#¡Asigna la variable total en la línea 8!

comida = 44.50#valor entero con centavos
impuesto = 0.0675#valores correspondientes a porcentajes, 6.75
propina = 0.15#15%

comida = comida + comida * impuesto
total= comida+comida*propina
#el total
print("%.2f" % total)