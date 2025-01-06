"""
Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas el nombre
del usuario tantas veces como el número introducido.
"""

print("Ejercicio 01")

def saludar(nombre,n_veces):
    return (nombre+"\n")*n_veces;

print(saludar("Jhonatan",3))
