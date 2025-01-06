"""
Escribir un programa que pregunte por consola el precio de un producto 
en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.
"""

precio = 12.34

# Convertimos el precio a euros y céntimos
def mostrar_euros_centimos(precio):
    euros = round(precio)
    centimos = str(precio)
    return f"El precio introducido tiene {euros} euros y {centimos[3:len(centimos)]} centimos "
        
print(mostrar_euros_centimos(precio))