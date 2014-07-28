'''Dos listas se pueden convertir en una sola'''
m = [1,2,3]
n = [4,5,6]
def myFun(x,y):
    v = m+n#las podemos unir solo con el simbol +
    return(v)
print ('Concateno dos listicas',myFun(m,n))

#--------------------------------------------------------------------------
'''Un numero indeterminado de listas, puede ser uno solo'''
m = [1,2,3]
n = [4,5,6]
o = [7,8,9]
def myFun(*args):#argumentos indefinidos
    v=[]#lista vacia ESENCIAL
    for i in args:#cuenta el numero de listas en los argumentos
        v+=i#agregamos cada lista nueva a v
    return (v)#v ahora es la gran lista

print ('Concateno listas indefinidas',myFun(m,n,o))

#----------------------------------------------------------------------------
'''Que pasa si hay una lista dentor deo tra lista? ES LO MISMO!'''
q = [[1,2,3],[4,5,6,7,8,9]]
def myFun(r):
    f=[]
    for i in r:
        f+=i
    return (f)

print ('Lista dentro de lista:',myFun(q))
