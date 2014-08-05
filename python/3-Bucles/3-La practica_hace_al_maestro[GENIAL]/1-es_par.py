def es_entero(x):
   num= round(x)
   if x-num==0:
      return (True)
   else:
      return (False)

print(es_entero(0))
print(es_entero(0.2))
print(es_entero(0.8))
print(es_entero(1.8))
print(es_entero(1))
print(es_entero(-1))
print(es_entero(5))
print(es_entero(-2.2))
print(es_entero(-5.8))


