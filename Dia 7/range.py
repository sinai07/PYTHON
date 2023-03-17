lista = [1, 2, 3, 4]

for numero in lista:
    print(numero)

print(" \n ")

# Pides un rango que llegue hasta 5
for numero in range(5):
    print(numero)

print(" \n ")

# Pides un rango que desde el 1 hasta el 5 (Pero no sale 5)

for numero in range(1, 5):
    print(numero)

print(" \n ")

# Pides desde 20 hasta 31 pero no sale 31

for numero in range(20, 31):
    print(numero)

# Establecer de que manera imprime los numeros, salteados

for numero in range(20, 30, 2):
    print(numero)


lista = list(range(1,101))
print(lista)

# Utilizando la función range(),
# crea en una única linea de código una lista formada
# por todos los números múltiplos de 3 desde el 3 al 300 (inclusive).
# Almacena dicha lista en la variable mi_lista.

mi_lista = list(range(3, 302, 3))


suma_cuadrados = 0

for i in range(1, 16):
    suma_cuadrados += i ** 2