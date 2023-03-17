# Esta es una manera de hacerlo
4 < 5
5 < 6

mi_bool = 4 < 5 < 6
print(mi_bool)

# Pero es mejor hacerlo de esta manera

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = (4*2 < 5) and (5 > 6+5)
print(mi_bool)

mi_bool = (55 == 55) and ("perro" == "perro")
print(mi_bool)

# Operador "OR" Si una de ellas no es verdadera, va a decir que es verdadera de igual forma.
# Para que diga falso, las dos deben ser falso
mi_bool = 10 == 10 or 3 == 3
print(mi_bool)

mi_bool = 10 == 10 or 3 == 4
print(mi_bool)

texto = "esta frase es breve"
mi_bool = "frase" in texto
print(mi_bool)

# Aqui no es como OR que no importa el resultado. Con in si importa
texto = "esta frase es breve"
mi_bool = ("frase" in texto) and ("amor" in texto)
print(mi_bool)


# El NOT

mi_bool = "a" == "a"
print(mi_bool)

mi_bool = not "a" == "a"
print(mi_bool)

mi_bool = not "a" != "a"
print(mi_bool)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = palabra1 and palabra2 not in frase
print(mi_bool)


frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = palabra1 in frase
dic = {False:"no"}
print(dic[mi_bool])