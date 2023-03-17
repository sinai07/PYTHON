lista = ["a", "b", "c", "d"]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

lista = ["a", "b", "c", "d"]

for item in enumerate(lista):
    print(item)
for indice,item in enumerate(lista):
    print(indice, item)

lista = ["a", "b", "c", "d"]
indice = 0

for item in enumerate(range(50,55)):
    print(indice,item)

#Taples

lista = ["a", "b", "c", "d"]

mis_tuples = list(enumerate(lista))
print(mis_tuples[1])


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


palabra = "python"
letra = []

for letra in palabra:
    print(letra)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in lista_nombres:
    if nombre == nombre.index[]:
        nombre == "M"
            print(nombre)