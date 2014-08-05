def inverso(texto):
   x=len(texto)
   word=''#esta variable guardara el texto
   while x>0:
      x-=1#le quitamos uno a x para darselo como indice
      word+=texto[x]#vamos agregando a la palabra
   #print(type(word))#--------------------------------------------------------> Debug
   return(word)

print(inverso('Python!'))
