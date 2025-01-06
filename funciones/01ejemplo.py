print("Hola Mundo")
# ENCONTRANDO EL NUMERO MAYOR DE UNA LISTA 
numeros = [4,5,-5,6,72]
numero_mas_alto = max(numeros)
numero_mas_bajo = min(numeros)

# como redondear un numero
numero_redondeado = round(12.34543,2)

# Todos los elementos son verdaderos
print(all([True, 1, "Hola"]))  # True (todos son evaluados como True)

# Al menos un elemento es falso
print(all([True, 0, "Hola"]))  # False (el 0 es evaluado como False)
print(all([False, 1, 2]))      # False (el False hace que el resultado sea False)

# Iterable vacío
print(all([]))                 # True (no hay elementos falsos)

# Ejemplo con strings
print(all(["Hola", "Mundo", ""]))  # False (la cadena vacía "" es False)

print(numero_mas_alto)
print(numero_mas_bajo)
print(numero_redondeado)