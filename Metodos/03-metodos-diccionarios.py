print("METODOS DE DICCIONARIO")

# creamos el diccionario
diccionario = {
    "nombre" : 'Jhonatan',
    "apellido" : 'Ojeda',
    "subs" : 800000
}

# devolver las claves
claves = diccionario.keys()
print(claves)
print(diccionario)

# devolver el valor de una clave
clave  = diccionario.get("nombre")
print(clave)

# obteniendo un elemento dic_items iterable
diccionario_iterable = diccionario.items()
print(diccionario)
print("")
# eliminando un elemento por clave
diccionario.pop("nombre")
diccionario.pop("apellido","subs")
print(diccionario_iterable)

# eliminando el diccionario 
diccionario.clear()
print(diccionario)
