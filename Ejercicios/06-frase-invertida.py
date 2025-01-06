"""
Escribir un programa que pida al usuario que introduzca una
frase en la consola y muestre por pantalla la frase invertida.
"""
print("Ejercicio 06")

def invertir_frase(frase):
    invertido = ""
    for i in range(len(frase)):
        invertido += frase[len(frase)-i-1];
    return invertido        
print(invertir_frase("hola"))

        
        
        