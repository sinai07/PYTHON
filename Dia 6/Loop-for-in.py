lista = ['a','b','c']

# Despues de for puede decir cualquier cosa pero es importate que se indique la misma palabra en print
for letra in lista:
    print("Letra: " + letra)

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"La letra {numero_letra}: es la letra {letra}")

lista = ["pablo", "laura", "fede", "luis", "julia"]

for nombre in lista:
    if nombre.startswith("l"):
        print(nombre)
    else:
        print("nombre que no comienza con l son: ", nombre)

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

# Si colocamos "print" en la linea que empieza solo va a imprimir el valor total de la operacion
for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

# Para imprimir cada letra de la palabra
palabra = "Python"

for letra in palabra:
    print(letra)

# Tambien puedes tener el mismo resultado sin indicar las variables
print("\n")
for letra in "python":
    print(letra)

# Iterar Listas q tenga lista

for objeto in [[1, 2], [3, 4], [5, 6]]:
    print(objeto)

# Si quiero imprimir todos y no por listas, puedo hacer lo siguiente


for a,f in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(f)

for a,f,m in [[1, 2, 4], [3, 4, 8], [5, 6, 6]]:
    print(a)
    print(f)
    print(m)

dic = {"clave1":"a", "clave2":"b", "clave3":"c"}

for item in dic:
    print(item)
# Imprimir todo el diccionario
for item in dic.items():
        print(item)

# Imprimir solo el significado o valor  del diccionario

for item in dic.values():
        print(item)

dic = {"clave1":"a", "clave2":"b", "clave3":"c"}

for a,g in dic.items():
    print(a,g)


# Recuerda que el item es la clave1 y el value es lo que vale el item