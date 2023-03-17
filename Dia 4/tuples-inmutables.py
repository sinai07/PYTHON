mi_tuple = (1,2,3,4)
print(type(mi_tuple))

print(mi_tuple[0])
print(mi_tuple[-2])

mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2])
print(mi_tuple[2][1])

mi_tuple = list(mi_tuple)

print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1,2,3)

x,y,z = t
print(x,y,z)

t = (1,2,3,1)
print(len(t))

print(t.count(1))
print(t.index(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
print(mi_tupla)

mi_lista = list(mi_tupla)

print(mi_lista)

mi_tupla = (1, 2, 3, 4)

a,b,c,d = mi_tupla
print(a,b,c,d)