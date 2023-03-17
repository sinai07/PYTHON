# Zip combina dos o mas listas entrelazando sus elementos en tuples (x, y)

nombre = ["Ana", "Hugo", "Valeria"]
edad = [65, 29, 42]
ciudades = ["lima", "Madrid", "Mexico"]
combinados = zip(nombre, edad)
print(combinados)

nombre = ["Ana", "Hugo", "Valeria"]
edad = [65, 29, 42]

combinados = list(zip(nombre, edad, ciudades))
print(combinados)

for nombre,edad,ciudades in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudades}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

capitales_del_mundo = list(zip(capitales, paises))

for capitales,paises in capitales_del_mundo:
    print(f"la capital del {paises} es {capitales}")


marcas = ["timberland", "Nike", "Adidas", "Brooks"]
productos = ["zapatos", "medias", "guantes", "pantalones"]

mi_zip = (zip(marcas, productos))
print(mi_zip)




espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]



numeros = list(zip(espanol, portugues, ingles))

for espanol,portugues,ingles in numeros:
    print(f"{espanol} en {portugues} y {ingles})

numeros = ["uno", "dos", "tres", "cuatro", "cinco"