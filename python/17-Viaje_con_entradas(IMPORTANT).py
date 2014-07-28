def costoHotel(dias):
#Calcula el costo del hotel por dias $140c/u
    return 140*dias
def costoViajeAvion(ciudad):
#Cuanto vale el boleto de avion, dependiendo de la ciudad
    if ciudad=="Charlotte":
        return 183
    elif ciudad=="Tampa":
        return 220
    elif ciudad== "Pittsburgh":
        return 222
    elif ciudad== "Los Angeles":
        return 475
    
def costoAlquilarAuto(dias):
#Cuanto cuesta el alquiler del coche, hay descuentos tambien
    costo= dias*40

    if dias>=7:
        costo-=50

    elif dias>=3:
        costo-=20
    return costo

def costoViaje(ciudad,dias,dineroGastos):
    return(costoAlquilarAuto(dias) + costoHotel(dias) + costoViajeAvion(ciudad) + dineroGastos)

city= input("Ingresa la ciudad")
day= int(input("Ingresa los dias"))
gastos= int(input("Ingresa tu saldo"))

print("Tu viaje es aproximadamente unos $",(costoViaje(city,day,gastos)))
#OJO el signo + aqui nos falla, usemos coma para concatenar

print("SEGUNDA VES, Tu viaje es aproximadamente unos $"+ str((costoViaje(city,day,gastos))))
#convertimso a string implicitamente, evitando el error
