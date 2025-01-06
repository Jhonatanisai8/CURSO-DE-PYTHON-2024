"""
Escribir un programa que pregunte el correo electrónico 
del usuario en la consola y muestre por pantalla otro correo 
electrónico con el mismo nombre (la parte delante de la arroba @)
pero con dominio ceu.es.
"""
print("Ejericicio 08")
def cambiar_dominio(correo):
    return correo.replace("gmail.com","ceu.es")

print(cambiar_dominio("correo@gmail.com"))