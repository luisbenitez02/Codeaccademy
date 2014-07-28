#Podemos importar solo uan funcion de una libreria
#A esto se le llama importacion de funcion
from math import sqrt
#gracias a esto solo tenemos que llamar a sqrt y no math.sqrt()
#la caja match se quedo en bodega y solo te trajeron la herramienta sqrt
#pero cuidado, si quieres importar otra cosa, debe ser tambien por separado

from math import *
"""En este ejemplo importamos toda la libreria, es como sacar todo de la caja
y ordenarlo, sin tener que llamar cada cosa desde math, pero eso traeria muchas
variables y funciones con todos sus nombres, no podras tenre una funcion sqrt
propia y otra de math pues se cruzaran"""

#es recomendable tener siempre el formato import.modulo
# e invocar cada funcion necesaria en el momento


