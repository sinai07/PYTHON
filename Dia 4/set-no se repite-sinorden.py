# puedes usar corchetes o no
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,}
print(type(otro_set))
print(otro_set)

# No pueden tener repeticiones. Si lo run, simplemente lo omite y print lo mismo
# No puedes poner listas
# No adimite diccionarions
# Si tuples

mi_set = set([1,2,3,(4,5,6),4,5])
print(mi_set)


# Puedes usar len

mi_set = set([1,2,3,(4,5,6),4,5])
print(len(mi_set))

# Saber si un item se encuentra en el Set

mi_set = set([1,2,3,(4,5,6),4,5])
print(2 in mi_set)

# Unir en sets y poner repetido pero no aparece repetido al imprimir
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# Agregar en Set con .add

s1 = {1, 2, 3}
s1.add(4)
print(s1)

# Remover en Set
s1.remove(2)
print(s1)

# Eliminar elemento aleatorio con pop

s1 = {1, 2, 3}
s1.pop()
print(s1)

# Limpiar en Set con clear

s1.clear()
print(s1)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

# Practica unir
mi_set_3 = mi_set_2.union(mi_set_1)
print(mi_set_3)

# Eliminar aleatorio
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

# Agregar en sets
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add("Damian")
print(sorteo)