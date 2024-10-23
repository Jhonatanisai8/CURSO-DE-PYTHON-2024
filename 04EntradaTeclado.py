print("Entrada de datos por consola")
name = input("¿Cual es tu nombre?: ")
edad = input("¿Cuantos años tienes?: ")

print(name)
print(edad)
print("Type: ",type(name))
print("Type: ",type(edad))

#cambiamos de valor
name = 123
edad = "Brais"

print("NUEVOS VALORES")
print(name)
print(edad)
print("Type nombre: ",type(name))
print("Type edad: ",type(edad))


#forzamos el tipo
direccion :str= "Mi direccion"
direccion = True
print("Direccion: ",direccion)
print("Type direccion: ",type(direccion))




