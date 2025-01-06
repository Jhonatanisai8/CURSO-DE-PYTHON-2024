"""Escribir un programa que pida al usuario que introduzca una frase 
en la consola y una vocal, y después muestre por pantalla la misma 
frase pero con la vocal introducida en mayúscula."""

print("Ejercicio 07")

def transformar_frase(frase,vocal):
    return frase.replace(vocal.lower(), vocal.upper())

print(transformar_frase("la vida es bella",'a'))