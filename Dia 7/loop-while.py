monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
else:
    print("no tengo mas dinero")

# Tambine puedes poner      monedas -= -1


respuesta = "yes"

while respuesta == "yes":
    respuesta = input("Quieres seguir? (yes/no) ")
else:
    print("gracias")

# Pass significa pasar y no necesita codigo

respuesta = "s"

while respuesta == "s":
    pass

print("Hola")

# Break para interrumpir la interaccion y salir del loop

nombre = input("Tu nombre ")

for letra in nombre:
    print(letra)

nombre = input("Tu nombre ")



