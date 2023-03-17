texto = "Este es el texto de Federico"
resultado = texto.split("t")
print(resultado)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)


texto = "Este es el texto de Federico"
resultado = texto.find("Federico")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("Federico", "Sinai")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("e","S")
print(resultado)
