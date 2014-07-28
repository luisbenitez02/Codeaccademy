def costoHotel(dias):
    """Calcula el costo del hotel por dias $140c/u"""
    return 140*dias

def costoViajeAvion(ciudad):
    """Cuanto vale el boleto de avion, dependiendo de la ciudad"""
    if ciudad== "Charlotte":
        return 183 
    elif ciudad== "Tampa":
        return 220 
    elif ciudad== "Pittsburgh": 
        return 222
    elif ciudad== "Los Angeles":
        return 475

def costoAlquilarAuto(dias):
    """Cuanto cuesta el alquiler del coche, hay descuentos tambien"""
    cost = dias*40
    if dias >= 7:
        cost -= 50
    elif dias >= 3:
        cost -= 20
    return cost 
    
def costoViaje(ciudad,dias,dineroGastos):
    """Calculo final con los valroes retornados de cada funcion"""
    return(costoAlquilarAuto(dias) + costoHotel(dias) + costoViajeAvion(ciudad) + dineroGastos)


print("Tu viajecito te saldra por unos $", costoViaje("Tampa",5,600))
#el simbolo mas es erroneamente interpretado por eso la coma
