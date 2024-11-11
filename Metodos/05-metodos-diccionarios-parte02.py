print("METODOS DE DICCIONARIOS EN PYTHON")
diccionario = {
    "nombre": "Sai Liz",
    "edad": 30,
    "ocupación": "Desarrollador de software",
    "email": "Sai.Liz@example.com",
    "teléfono": "+1-555-1234",
    "calle": "Calle Falsa 123",
    "ciudad": "Ciudad Ejemplo",
    "país": "País Ejemplo",
    "código_postal": "12345"
}

# dict.copy() => Retorna una copia superficial del diccionario.
diccionario_copia = diccionario.copy()
print(f"Diccionario Copia: {diccionario_copia}")

# dict.fromkeys(iterable, value=None)
# Crea un nuevo diccionario con las claves del iterable y asigna a todas el mismo valor.
diccionario_keys = {'a','b','c'}
nuevo_diccionario = dict.fromkeys(diccionario_keys,0)
print(f"Nuevo diccionario =>: {nuevo_diccionario}")

# dict.get(key, default=None)
# Retorna el valor de la clave especificada. Si la clave no existe, retorna el valor por defecto.
diccn= {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}
print(diccn.get('a'))      # Resultado: 1
print(diccn.get('c', 0))   # Resultado: 3


# dict.items()
# Retorna una vista de los pares clave-valor en el diccionario como tuplas.
diccionario_clave_valor = diccionario_copia.items()
print(f"Diccinario: {diccionario_clave_valor}")

# dict.keys()
# Retorna una vista de las claves en el diccionario.
dic = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}
print(f"Claces del diccionario => {dic.keys()}")

# dict.pop(key, default=None)
# Elimina y retorna el valor asociado con la clave especificada. Si la clave no existe, retorna el valor por defecto.
d = {'a': 1, 'b': 2}
print(d.pop('a'))
print(d)

# dict.popitem()
# Elimina y retorna un par clave-valor aleatorio como una tupla. Es útil para extraer elementos si no importa el orden.
d = {'a': 1, 'b': 2}
print("d.popitem() => ",d.popitem())
# Resultado: ('a', 1) o ('b', 2), dependiendo del orden


# dict.setdefault(key, default=None)
# Retorna el valor de la clave si existe; si no, inserta la clave con el valor por defecto y la retorna.
d = {'a': 1}
print(d.setdefault('a', 0))  # Resultado: 1
print(d.setdefault('b', 0))  # Resultado: 0
print(d)                     # Resultado: {'a': 1, 'b': 0}

# dict.update(other_dict)
# Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable de pares
d = {'a': 1}
d.update({'b': 2, 'c': 3})
# Resultado: {'a': 1, 'b': 2, 'c': 3}

# dict.values()
# Retorna una vista de todos los valores en el diccionario.
d = {'a': 1, 'b': 2}
print("Valores => ",d.values())
# Resultado: dict_values([1, 2])

# dict.clear()
# Vacía todos los elementos del diccionario.
persona = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ocupación": "Desarrollador de software",
    "email": "juan.perez@example.com",
    "teléfono": "+1-555-1234"
}
print("Diccionario Actualizado => ",persona)
persona.clear()
print("Diccionario Actualizado => ",persona)