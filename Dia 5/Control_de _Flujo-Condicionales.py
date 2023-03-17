# Solo verificar si es verdadero o  falso
if 10 > 9:
    print("Es correcto")

# Aqui if se esta dandso cuenta que hay un valor verdadero o falso, entonces si ponemos esto abajo uigual sera
x = True
if x:
    print("es correcto")

if 5 == 2:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "Elefante"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No se que animal tienes")

edad = 16
calificacion = 9

if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres mayor de edad")


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"num1 es mayor que num2")
elif num2 > num1:
    print(f"num2 es mayor que num1")
else:
    print(f"num1 y num2 son iguales")


#"Puedes conducir"

#"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

#"No puedes conducir. Necesitas contar con una licencia"


edad = int(input("Que edad tienes: "))
tiene_licencia = input("Tienes licencia de conducir: ") == "no"
print(edad)


if edad > 18 and tiene_licencia == "yes":
    print("puedes conducir")
elif edad < 18 and tiene_licencia == "no":
    print("No puedes conducir aun. Debes tener 18 anos y contar con licencia")
elif edad == 18 and tiene_licencia == "no":
    print("No puedes conducir.Necesitas una licencia")

