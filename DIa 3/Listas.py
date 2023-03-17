mi_lista =  ['a','b','c']
resultado = len(mi_lista)
print(resultado)

mi_lista =  ['a','b','c']
resultado = mi_lista[0]
print(resultado)

mi_lista =  ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'

print(mi_lista3)

resultado = mi_lista[0:1]
print(resultado)

mi_lista =  ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')

eliminado = mi_lista3.pop(0)

print(mi_lista3)
print(eliminado)


#ordenar la lista

lista = ['g','o','b','m','c']
lista.sort()
lista.reverse()
print(lista)


