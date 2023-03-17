var1 = True
var2 = False
print(type(var1))
print(var1)

# Falso 5 no es mayor que 5 con >
numero = 5 > 2+3
print(type(numero))
print(numero)

# Igual que con ==
numero = 5 == 2+3
print(numero)

# Mayor o igual con >=
numero = 5 >= 2+3
print(numero)

# Diferentes con !=
numero = 5 != 2+3
print(numero)

numero = bool(5<6)
print(numero)

# Preguntar a Python si hay un numero en una lista

lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)

control = 5 not in lista
print(type(control))
print(control)

numero = 7 > 3 * 8
prueba = numero
print(prueba)

prueba = bool(7 > 3*8)
print(prueba)

numero = 25**(0.5) == 5
print (numero)