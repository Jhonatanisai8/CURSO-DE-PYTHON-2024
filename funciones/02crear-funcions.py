print("CREANDO MIS PROPIAS FUNCIONES")

# primera funcion creada
def saludar(nombre):
    return f"Hola {nombre}"

def sumar(n1,n2):
    return n1+n2


saludo = saludar("Jhonatan")
suma = sumar(1,2)
print(saludo)
print(suma)
print(type(saludo))
print(type(suma))