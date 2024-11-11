print("DESEMPAQUETADO EN PYTHON")

# creando los datos
datos_en_tupla = ("Jhonatan Isai","Ojeda",120)

# desempaquetando los datos
nombres,apellido,edad = datos_en_tupla

# mostramos las variables
print(nombres)
print(apellido)
print(edad)

"""
Desempaquetado parcial (usando *)
Puedes capturar un subconjunto de los valores con el operador *. Esto es útil cuando no necesitas todos los elementos:
"""
valores = [1, 2, 3, 4, 5]
a, *b, c = valores
# Resultado: a = 1, b = [2, 3, 4], c = 5
print(a)
print(b)
print(c)


"""
Desempaquetado con listas y tuplas
También se puede hacer el desempaquetado en listas o estructuras similares:
"""
valores = [10, 20, 30]
x, y, z = valores
# Resultado: x = 10, y = 20, z = 30
print(x)
print(y)
print(z)
