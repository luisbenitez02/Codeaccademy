def por_tres(n):
    if n%3 == 0:
        cubo(n)#llmamos otra funcion y le pasamos n

def cubo(n):
    n= n**3
    print(n)

por_tres(9)
