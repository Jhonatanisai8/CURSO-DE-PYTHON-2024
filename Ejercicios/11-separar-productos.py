"""
Escribir un programa que pregunte por consola por los productos 
de una cesta de la compra, separados por comas, y muestre por pantalla
cada uno de los productos en una línea distinta
"""


productos = "lima,mango,limon,agua"

def separar_productos(productos):
    return productos.replace(",","\n")

print(separar_productos(productos))
print(type(separar_productos(productos)))
