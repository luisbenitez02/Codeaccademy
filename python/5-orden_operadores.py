# ¡Asigna los valores `True` o `False` en las líneas siguientes según corresponda!
"""El orden de operadores es el siguiente:
1. Se calcula not (a la derecha)
2.Se calcula and(ambos lados)
3.Se calcula or (ambos lados)

Si la operacion esta entre parentesis esta tiene prioridad
el doble operador not evalua dos veces y aria el resultado
ej:
not not True = True
not True = False"""
# False or not True and True
bool_one = False
# False and not True or True
bool_two = True
# True and not (False or False)
bool_three = True
# not not True or False and not True
bool_four = True
# False or not (True and True)
bool_five = False

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)
"""El operador not siempre va DESPUES de un and o un or o da error de sintaxis"""
