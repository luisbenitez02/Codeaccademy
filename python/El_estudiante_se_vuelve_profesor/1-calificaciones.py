Lloyd = {
    "nombre":"Lloyd",
    "tareas": [90,100,50,30],
    "pruebas": [88,40,94],
    "exámenes": [75,90]
    }
Alice = {
    "nombre":"Alice",
    "tareas": [100,92,98,100],
    "pruebas": [82,83,91],
    "exámenes": [89,97]
    }
Tyler = {
    "nombre":"Tyler",
    "tareas": [0,87,7522],
    "pruebas": [0,75,78],
    "exámenes": [100,100]
    }
estudiantes=[Lloyd,Alice,Tyler]

for i in estudiantes:
    print ('Estudiante:',i['nombre'])
    print ('Homeworks:',i['tareas'])
    print ('pruebas:',i['pruebas'])
    print ('Exámenes:',i['exámenes'])
