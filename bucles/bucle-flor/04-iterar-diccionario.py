print("iterando sobre un diccionario")

diccionario = {
    "nombre" : "fran",
    "apellido": "Lopex",
    "edad" : "34"
}

print(diccionario)
print(type(diccionario))

# iterando el diccionario 
for key in diccionario.items():
    print(f"clave: {key}")
    
# otra forma de iterar diccionario, obtenemos las claves y valores 
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]
    print(f"clave: {clave} ,valor {valor}")
    
print("iterando el diccionario para obtener las claves")
for clave in diccionario:
    print(f"clave : {clave.upper()}")