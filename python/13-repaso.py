def apagado(s):
    s= s.lower()#convertimos todo en minuscula
    if s=="si":
        print ("Apagando...")
        return ("Apagando...")
    elif s=="no":
        print("¡Apagado cancelado!")
        return ("¡Apagado cancelado!")
    else:
        print("Lo siento, no te entendí.")
        return ("Lo siento, no te entendí.")

azul= input("Deseas Apgar la maquina? si/no")#pedimos dato al usuario
apagado(azul)#le pasamos lo ingresado a la funcion apagado
