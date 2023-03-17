diccionario = {"c1":"valor1","c2":"valor2"}
print(type(diccionario))
print(diccionario)

resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre":"Juan","Apellido":"Fuentes","Peso":88,"talla":1.76}
consulta = (cliente["Apellido"])
print(consulta)


dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
print(dic["c2"][2])

dic = {"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic["c2"][1].upper())

dic = {"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic["c1"][0].upper())

dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2]= 'B'
print(dic.keys())
print(dic.values())
print(dic.items())