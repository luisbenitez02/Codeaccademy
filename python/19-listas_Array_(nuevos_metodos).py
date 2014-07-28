lenguajes_geniales=["python", "Ruby On Rails", "Javascript", "Swift", "Java", "node.js"]
print("Esta era la lista antes de modificarla: \n",lenguajes_geniales)

#FUNCION index() busca un string dentro del array y me devuelve su posicion en un int
me_gusta= lenguajes_geniales.index("Javascript")
print("Este el el numero de indice donde se ubica Javascript, dentro del array: \n ", me_gusta)

#agregaremos un nuevo elemento al Array PERO EN LA MITAD DE ESTE
#tomaremos el valor que devuelve la funcion index() y lo cambiaremos por otro string
#todo esto usando la funcion insert() añade un elemento en el lugar que deseemos

lenguajes_geniales.insert(me_gusta,"HTML5")
#me_gusta contiene un numero entero NO una variable completa de tipo array nam[i]
print("Ahora que modificamos la lista, se ve asi: \n", lenguajes_geniales)
print("Viste como agregamos HTML5 en la mitad de toda esa lista? Genial!")
