
edad = int(input("Que edad tienes: "))
tiene_licencia = input("Tienes licencia de conducir: ")

if edad >= 18 and tiene_licencia == "yes":
    print("puedes conducir")
elif edad >= 18 and tiene_licencia == "no":
    print("No puedes conducir aun. Debes contar con licencia")
elif edad < 18:
    print("no puedes conducir")

else:
    print("No puedes conducir.Necesitas una licencia")


habla_ingles = input("Hablas Ingles?: ")
sabe_python = input("Sabes python?: ")



if habla_ingles == "yes" and sabe_python == "yes":
    print("Cumples con los requisitos para postularte")
elif habla_ingles == "Yes" and sabe_python == "no":
    print("Para postularte necesitas saber Python")
elif habla_ingles == "no" and sabe_python == "yes":
    print("Para postularte necesitas saber Ingles")
elif habla_ingles == "no" and sabe_python == "no":
    print("Para postularte necesitas tener conocimientos de ingles y Python")
