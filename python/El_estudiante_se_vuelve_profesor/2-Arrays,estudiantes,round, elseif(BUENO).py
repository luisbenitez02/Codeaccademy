#Diccionarios, clave valor, contienen el nombre y las calificaciones definidas por tipo de trabajo
Luis={
'nombre':'Luis',
'tareas':[90,97,75,92],
'pruebas':[88,40,94],
'examenes':[75,90]
}

Patricia={'nombre':'Patricia',
'tareas':[100,92,6,100],
'pruebas':[8,83,12],
'examenes':[15,20]
}

Hernando={
'nombre':'Hernando',
'tareas':[0,87,75,22],
'pruebas':[80,75,78],
'examenes':[100,100]
}
#la variable estudiantes nos ayudara en su paso por el ciclo y asi miraremos cada calificacion
#la ponemos despues de HABER DEFINIDO las variables con los diccionarios
estudiantes= [Luis,Patricia,Hernando]
def promedio(dato):
    #devuelve el promedio por tipo de trabajo, recibe como dato estudiante['tipodetarea']
    return (sum(dato))/(len(dato))

def calcularPromedio(chico):
    #calcula el promedio global, teniendo en cuenta el porcentaje de cada trabajo
    #luego llama a la funcion que asigna una calificacion escrita
    cu=promedio
    n=cu(chico["tareas"])*0.1 + cu(chico["pruebas"])*0.3 + cu(chico["examenes"])*0.6
    #califica_letras(n)
    return(n)

def califica_letras(nota):
    #redondeamos y le asignamos otro nombre a la variable, devolvemos un string
    red= round(nota)
    if red >= 80:
        #print('¡Excelente!')
        return('¡Excelente!')
    elif 60 < red < 80:
        print('Sobresaliente')
        return('Sobresaliente!')
    elif 40 < red < 60:
        #print('Aceptable')
        return('Aceptable')
    elif 20 < red < 40:
        #print('Rodilleras ON')
        return('Rodilleras ON')
    elif red < 20:
        #print('Deficiente')
        return('Deficiente')


def calcularPromedioClase(estudiantes):
    #Por medio de un ciclo for llamamos a todas los valroes del ddiccionario
    #le entr3egamos esos valores llamando a las diferentes funciones
    #y sumamos el promeido general del curso
    counta=0#cuenta las vueltas del for para asi poder dividir el promedio
    final=0
    for i in estudiantes:
        print('Calificaciones de', i['nombre'])
        print('Tareas 10%:', promedio(i['tareas']))
        print('Pruebas 30%:', promedio(i['pruebas']))
        print('Examenes 60%:', promedio(i['examenes']))
        print('Promedio de notas ponderado:',calcularPromedio(i))
        print('Estado:',califica_letras(calcularPromedio(i)))
        final+=calcularPromedio(i)
        counta+=1
        print()
    print('promedio curso:', round(final/counta))

calcularPromedioClase(estudiantes)#le pasamos la lista estudiantes y ejecutamos todas las funciones partiendo de una sola
