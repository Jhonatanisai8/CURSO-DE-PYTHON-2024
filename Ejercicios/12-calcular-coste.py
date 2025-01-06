"""
Escribir un programa que pregunte el nombre el un producto, 
su precio y un número de unidades y muestre por pantalla una 
cadena con el nombre del producto seguido de su precio unitario 
con 6 dígitos enteros y 2 decimales, el número de unidades con 
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

print("Ejercicio 12")

producto = "limon"
precio = 23.4
unidades = 3

print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))