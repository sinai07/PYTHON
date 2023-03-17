# Generar el texto que el usuario va a escribir con input
texto = input("Ingresa un texto a eleccion: ")

# Letras que el usuario va a ingresar
letras = []

# El texto debe transformarse en minusculas
texto = texto.lower()

# Pedir usuario las letras y almacenarlas en la lista: Lo que ingrese el usuario debe trasnformar en minuscuila con .lower

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

# Cantidad de letras en el texto
print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(len(texto))
print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")


print("\n")
print("Cantidad de Palabras: ")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("Letras de inicio y de fin: ")
letras_de_inicio = texto[0]
letras_final = texto[-1]
print(f"La letras de inicio es {letras_de_inicio} y la letras final es {letras_final}")

print("\n")
print("Texto invertido es: ")

palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto de manera invertida, obtendras la siguiente oracion: '{texto_invertido}'")

print("\n")
print("Buscando la palbra Python")
buscar_python = "python" in texto
dic = {False:"no", True:"Si"}
print(f"La palabra python {dic[buscar_python]} se encuentra en texto")
