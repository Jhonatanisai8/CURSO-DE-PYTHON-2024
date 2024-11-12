print("CREACION Tuplas")

# creamos la tupla con una funcion tuple
tupla = tuple(["Hola","Mundo",12])
print(f"Datos de la tupla =>: {tupla}")

"""Crear una tupla sin paréntesis
Python permite omitir los paréntesis al crear tuplas; 
simplemente separa los elementos por comas:"""
mi_tupla = 12,45,"Hola"
print(f"Datos de la tupla =>: {mi_tupla}")

"""Usar el constructor tuple()
También puedes crear una tupla usando el constructor tuple(), 
que convierte cualquier iterable en una tupla."""
mi_lista_frutas = {"limon","mango","cereza"}
mi_tupla_frutas = tuple(mi_lista_frutas)
print(f"mi tupla de frutas: {mi_tupla_frutas}")

"""Tuplas anidadas
Puedes tener tuplas dentro de otras tuplas, lo que se conoce como tuplas anidadas:"""
mi_tupla_anidada = (1,("limon","Mango"),(45,67))
print(f"Mi tupla anidada: {mi_tupla_anidada}")

"""Crear una tupla con un solo elemento
Para crear una tupla con un solo elemento, debes agregar una coma después del elemento. 
Si no incluyes la coma, Python la interpretará como un tipo básico 
(por ejemplo, un número o una cadena)."""
mi_tupla_un_elemento = (5,)
print(f"Mi tupla de un solo elemento es: {mi_tupla_un_elemento}")

"""Crear una tupla vacía
Para crear una tupla vacía, usa simplemente paréntesis vacíos:"""
mi_tupla_vacia = ()
print(f"Datos de mi tupla: {mi_tupla_vacia}")

mi_tupla_ciudades = "lima","chiclayo","los olivos","comas"
print(mi_tupla_ciudades.index("chiclayo")) #=> nuestra el indice en el que esta el valor
