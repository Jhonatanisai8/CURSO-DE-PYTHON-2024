# VARIABLES
print("Variables en Python")

my_variable = "Esta es mi variable"
my_edad = 3
my_boo = True

print(my_variable)
print(my_edad)
print(my_boo)

# concatenacion de variables
print(my_variable,my_edad,my_boo)

print("Convertir int a str")
numero_celular = str(my_edad)
print(numero_celular)
print(type(numero_celular))

#funciones del sistema
my_nombre = "Jhonatan"
print(len(my_nombre))

my_luga_nacimiento = "Sullana"
print("Este es el valor de: ",my_luga_nacimiento)

# variables en una sola linea
nombre, apellido, alias, edad = "Jhonatan Isai", "Ojeda Sanchez", "Jhomy", 18

print("Me llamo: ",nombre,apellido,". Mi edad es: ",edad," y mi apodo es: ",alias)

ciudad = "Tambogrande"
anio = 2024
bienvenida = f"Hola {ciudad} ¿Como estas? {anio}"
print(bienvenida)
print("Hola " in bienvenida)